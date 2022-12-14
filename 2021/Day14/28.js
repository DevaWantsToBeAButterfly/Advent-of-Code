puzzleAlchemyArray = [['OO', 'N'], ['VK', 'B'], ['KS', 'N'], ['PK', 'H'], ['FB', 'H'], ['BF', 'S'], ['BB', 'V'], ['KO', 'N'], ['SP', 'K'], ['HK', 'O'], ['PV', 'K'], ['BP', 'O'], ['VO', 'V'], ['OP', 'C'], ['BS', 'V'], ['OK', 'V'], ['KN', 'H'], ['KC', 'N'], ['PP', 'F'], ['NB', 'V'], ['CH', 'V'], ['HO', 'K'], ['PN', 'H'], ['SS', 'O'], ['CK', 'P'], ['VV', 'K'], ['FN', 'O'], ['BH', 'B'], ['SC', 'B'], ['HH', 'P'], ['FO', 'O'], ['CC', 'H'], ['OS', 'H'], ['FP', 'S'], ['HC', 'F'], ['BO', 'F'], ['CF', 'S'], ['NC', 'S'], ['HS', 'V'], ['KF', 'O'], ['ON', 'C'], ['CN', 'K'], ['VF', 'F'], ['NO', 'K'], ['CP', 'N'], ['HF', 'K'], ['CV', 'N'], ['HN', 'K'], ['VH', 'B'], ['KK', 'P'], ['CS', 'O'], ['VS', 'P'], ['NH', 'F'], ['CB', 'S'], ['BV', 'P'], ['FK', 'F'], ['NV', 'O'], ['OV', 'K'], ['SB', 'N'], ['NF', 'O'], ['VN', 'S'], ['OH', 'O'], ['PS', 'N'], ['HB', 'H'], ['SV', 'V'], ['CO', 'H'], ['SO', 'P'], ['FV', 'N'], ['PF', 'O'], ['NN', 'S'], ['KB', 'P'], ['NP', 'F'], ['OC', 'S'], ['FS', 'P'], ['FH', 'P'], ['VP', 'K'], ['BN', 'O'], ['NS', 'H'], ['VB', 'V'], ['PO', 'K'], ['KP', 'N'], ['SN', 'O'], ['BC', 'H'], ['SF', 'V'], ['PC', 'O'], ['NK', 'F'], ['BK', 'V'], ['KH', 'S'], ['SH', 'S'], ['SK', 'H'], ['OB', 'V'], ['PH', 'N'], ['PB', 'C'], ['HV', 'N'], ['HP', 'V'], ['FF', 'B'], ['OF', 'P'], ['VC', 'S'], ['KV', 'C'], ['FC', 'F']]

puzzleStart = new Map([['HH', 1], ['HK', 1], ['KO', 1], ['ON', 2], ['NS', 2], ['SO', 2], ['OS', 1], ['SV', 1], ['VO', 1], ['OF', 1], ['FC', 1], ['CS', 1], ['SC', 1], ['CN', 1], ['NB', 1], ['BC', 1]])

alphabet = 'BCFHKNOPSV'

letterCounts = new Map()

for (letter of alphabet) {
	letterCounts.set(letter, 0)
}
letterCounts.set('H', 2)
letterCounts.set('K', 1)
letterCounts.set('N', 3)
letterCounts.set('S', 4)
letterCounts.set('C', 3)
letterCounts.set('V', 1)
letterCounts.set('F', 1)
letterCounts.set('B', 1)

function writeAlchemyMap(alchArray) {
	alchemyMap = new Map()
	for ([key, value] of alchArray) {
		alchemyMap.set(key, value)
	}
	return alchemyMap
}

function doPolymerization(alchMap, currentMap, turnsToPlay) {
	for (t = 1; t <= turnsToPlay; t++) {
		currentMap = elaborateSingleStep(alchMap, currentMap)
	}
}

function elaborateSingleStep(alchemyMap, currentStateMap) {
	updatedMap = new Map()
	for ([key, value] of currentStateMap) {
		spawnedElement = alchemyMap.get(key)
		reactionsCount = value
		newPair = key[0] + spawnedElement
		currentPairCount = updatedMap.get(newPair)
		if (currentPairCount) {
			updatedMap.set(newPair, reactionsCount + currentPairCount)
		} else {
			updatedMap.set(newPair, reactionsCount)
		}

		newPair = spawnedElement + key[1]
		currentPairCount = updatedMap.get(newPair)
		if (currentPairCount) {
			updatedMap.set(newPair, reactionsCount + currentPairCount)
		} else {
			updatedMap.set(newPair, reactionsCount)
		}

		currentLetterCount = letterCounts.get(spawnedElement)
		letterCounts.set(spawnedElement, currentLetterCount + reactionsCount)
	}
	return updatedMap
}

function getMaxMin(elementsCount) {
	mostCommonElement = Math.max(...elementsCount.values())
	leastCommonElement = Math.min(...elementsCount.values())
	console.log(mostCommonElement, leastCommonElement)
	console.log(mostCommonElement - leastCommonElement)
}

alchemyMap = writeAlchemyMap(puzzleAlchemyArray)
doPolymerization(alchemyMap, puzzleStart, 400)

getMaxMin(letterCounts)