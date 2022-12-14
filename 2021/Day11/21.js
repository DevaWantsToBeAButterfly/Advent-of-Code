testInput = [[5, 4, 8, 3, 1, 4, 3, 2, 2, 3], [2, 7, 4, 5, 8, 5, 4, 7, 1, 1], [5, 2, 6, 4, 5, 5, 6, 1, 7, 3], [6, 1, 4, 1, 3, 3, 6, 1, 4, 6], [6, 3, 5, 7, 3, 8, 5, 4, 7, 8], [4, 1, 6, 7, 5, 2, 4, 6, 4, 5], [2, 1, 7, 6, 8, 4, 1, 7, 2, 1], [6, 8, 8, 2, 8, 8, 1, 1, 3, 4], [4, 8, 4, 6, 8, 4, 8, 5, 5, 4], [5, 2, 8, 3, 7, 5, 1, 5, 2, 6]]

puzzleInput = [[4, 4, 7, 2, 5, 6, 2, 2, 6, 4], [8, 6, 3, 1, 5, 1, 7, 8, 2, 7], [7, 2, 3, 2, 1, 4, 4, 1, 4, 6], [2, 4, 4, 7, 1, 6, 3, 8, 2, 4], [1, 2, 3, 5, 2, 7, 2, 6, 7, 1], [5, 1, 3, 3, 5, 2, 7, 1, 4, 6], [6, 5, 1, 1, 3, 7, 2, 4, 1, 7], [3, 8, 4, 1, 8, 4, 1, 6, 1, 4], [8, 6, 2, 1, 3, 6, 8, 7, 8, 2], [3, 2, 4, 6, 3, 3, 6, 6, 7, 7]]

let totalFlashes = 0

function flashSquids(mapSnapshot) {
	chainReaction = false
	updatedMap = mapSnapshot.slice()
	for (let rowIndex = 0; rowIndex < mapSnapshot.length; rowIndex++) {
		row = mapSnapshot[rowIndex]
		for (let squidIndex = 0; squidIndex < row.length; squidIndex++) {
			squid = row[squidIndex]
			if (squid >= 10 && squid < 100) {
				totalFlashes++
				for (let r = -1; r <= 1; r++) {
					for (let c = -1; c <= 1; c++) {
						targetRowIndex = rowIndex + r
						targetSquidIndex = squidIndex + c
						if (targetRowIndex < 0 || targetRowIndex >= updatedMap.length || targetSquidIndex < 0 || targetSquidIndex >= row.length || (r === 0 && c === 0)) {
							continue
						}

						chargedSquid = updatedMap[targetRowIndex][targetSquidIndex] += 1
						updatedMap[targetRowIndex][targetSquidIndex] = chargedSquid
						if (chargedSquid === 10) {
							chainReaction = true
						}
					}
				}
				updatedMap[rowIndex][squidIndex] = 100
			}
		}
	}
	return [updatedMap, chainReaction]
}

function fixFlashedSquids(squidMap) {

	cleanedMap = squidMap
	partialFlashes = 0
	allSquidsFlashed = false

	for (let r = 0; r < squidMap.length; r++) {
		for (let s = 0; s < squidMap[r].length; s++) {
			squid = squidMap[r][s]
			if (squid >= 100) {
				cleanedMap[r][s] = 0
				partialFlashes++
			}
		}
	}
	if (partialFlashes === (squidMap.length * squidMap[0].length)) {
		allSquidsFlashed = true
	}
	return [cleanedMap, allSquidsFlashed]
}

function bumpAllSquids(oldMap) {
	newMap = oldMap.slice()
	for (let r = 0; r < oldMap.length; r++) {
		row = oldMap[r]
		for (let s = 0; s < row.length; s++) {
			bumpedSquid = newMap[r][s] += 1
			newMap[r][s] = bumpedSquid
		}
	}
	return newMap
}
function solveSingleTurn(squidMap, chainReaction) {

	squidMap = bumpAllSquids(squidMap)

	while (chainReaction) {
		stepOutcomes = flashSquids(squidMap)
		squidMap = stepOutcomes[0]
		chainReaction = stepOutcomes[1]
		isFirstStep = false
	}

	turnResults = fixFlashedSquids(squidMap)

	return turnResults
}

function simulateSquids(map, turns) {
	for (let t = 1; t <= turns; t++) {
		turnResults = solveSingleTurn(map, true)
		map = turnResults[0]
		if (turnResults[1]) {
			console.log('All squids flashed on turn ' + t)
		}
	}

	return map
}

thing = simulateSquids(puzzleInput, 1000)
console.log(thing)
console.log(totalFlashes)