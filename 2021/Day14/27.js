testAlchemyArray = [['CH', 'B'], ['HH', 'N'], ['CB', 'H'], ['NH', 'C'], ['HB', 'C'], ['HC', 'B'], ['HN', 'C'], ['NN', 'C'], ['BH', 'H'], ['NC', 'B'], ['NB', 'B'], ['BN', 'B'], ['BB', 'N'], ['BC', 'B'], ['CC', 'N'], ['CN', 'C']]

puzzleAlchemyArray = [['OO', 'N'], ['VK', 'B'], ['KS', 'N'], ['PK', 'H'], ['FB', 'H'], ['BF', 'S'], ['BB', 'V'], ['KO', 'N'], ['SP', 'K'], ['HK', 'O'], ['PV', 'K'], ['BP', 'O'], ['VO', 'V'], ['OP', 'C'], ['BS', 'V'], ['OK', 'V'], ['KN', 'H'], ['KC', 'N'], ['PP', 'F'], ['NB', 'V'], ['CH', 'V'], ['HO', 'K'], ['PN', 'H'], ['SS', 'O'], ['CK', 'P'], ['VV', 'K'], ['FN', 'O'], ['BH', 'B'], ['SC', 'B'], ['HH', 'P'], ['FO', 'O'], ['CC', 'H'], ['OS', 'H'], ['FP', 'S'], ['HC', 'F'], ['BO', 'F'], ['CF', 'S'], ['NC', 'S'], ['HS', 'V'], ['KF', 'O'], ['ON', 'C'], ['CN', 'K'], ['VF', 'F'], ['NO', 'K'], ['CP', 'N'], ['HF', 'K'], ['CV', 'N'], ['HN', 'K'], ['VH', 'B'], ['KK', 'P'], ['CS', 'O'], ['VS', 'P'], ['NH', 'F'], ['CB', 'S'], ['BV', 'P'], ['FK', 'F'], ['NV', 'O'], ['OV', 'K'], ['SB', 'N'], ['NF', 'O'], ['VN', 'S'], ['OH', 'O'], ['PS', 'N'], ['HB', 'H'], ['SV', 'V'], ['CO', 'H'], ['SO', 'P'], ['FV', 'N'], ['PF', 'O'], ['NN', 'S'], ['KB', 'P'], ['NP', 'F'], ['OC', 'S'], ['FS', 'P'], ['FH', 'P'], ['VP', 'K'], ['BN', 'O'], ['NS', 'H'], ['VB', 'V'], ['PO', 'K'], ['KP', 'N'], ['SN', 'O'], ['BC', 'H'], ['SF', 'V'], ['PC', 'O'], ['NK', 'F'], ['BK', 'V'], ['KH', 'S'], ['SH', 'S'], ['SK', 'H'], ['OB', 'V'], ['PH', 'N'], ['PB', 'C'], ['HV', 'N'], ['HP', 'V'], ['FF', 'B'], ['OF', 'P'], ['VC', 'S'], ['KV', 'C'], ['FC', 'F']]

testStart = 'NNCB'
puzzleStart = 'HHKONSOSONSVOFCSCNBC'
function writeAlchemyMap(alchArray) {
	alchemyMap = new Map()
	for ([key, value] of alchArray) {
		alchemyMap.set(key, value)
	}
	return alchemyMap
}

function doPolymerization(alchState, alchArray, turnsToGo) {
	alchemyMap = writeAlchemyMap(alchArray)

	for (let t = 1; t <= turnsToGo; t++) {
		alchState = singlePolymerizationStep(alchState, alchemyMap)
	}

	polyOutcome = alchState

	elementsList = new Set(polyOutcome)
	elementsCount = countElements(elementsList, polyOutcome)
	getMaxMin(elementsCount)
}

function singlePolymerizationStep(currentState, alchemyMap) {
	totalAdditions = 0
	updatedState = currentState.slice()
	for (let i = 0; i < currentState.length - 1; i++) {
		currentCombo = currentState.slice(i, i + 2)


		if (polyResult) {
			totalAdditions++
			updatedState = addPolyResult((i + totalAdditions), updatedState, polyResult)
		}
	}

	return updatedState
}

function addPolyResult(position, currentState, thingToAdd) {
	updatedState = currentState.slice(0, position) + thingToAdd + currentState.slice(position)

	return updatedState
}

function countElements(elementsList, polyOutcome) {
	elementsCounter = new Map()
	for (element of elementsList) {
		elementsCounter.set(element, 0)
	}
	for (element of polyOutcome) {
		currentCount = elementsCounter.get(element)
		elementsCounter.set(element, currentCount + 1)
	}
	return (elementsCounter)
}
function getMaxMin(elementsCount) {
	mostCommonElement = Math.max(...elementsCount.values())
	leastCommonElement = Math.min(...elementsCount.values())
	console.log(mostCommonElement, leastCommonElement)
	console.log(mostCommonElement - leastCommonElement)
}

doPolymerization(testStart, testAlchemyArray, 10)