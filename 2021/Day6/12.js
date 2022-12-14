puzzleInput = [2, 1, 1, 4, 4, 1, 3, 4, 2, 4, 2, 1, 1, 4, 3, 5, 1, 1, 5, 1, 1, 5, 4, 5, 4, 1, 5, 1, 3, 1, 4, 2, 3, 2, 1, 2, 5, 5, 2, 3, 1, 2, 3, 3, 1, 4, 3, 1, 1, 1, 1, 5, 2, 1, 1, 1, 5, 3, 3, 2, 1, 4, 1, 1, 1, 3, 1, 1, 5, 5, 1, 4, 4, 4, 4, 5, 1, 5, 1, 1, 5, 5, 2, 2, 5, 4, 1, 5, 4, 1, 4, 1, 1, 1, 1, 5, 3, 2, 4, 1, 1, 1, 4, 4, 1, 2, 1, 1, 5, 2, 1, 1, 1, 4, 4, 4, 4, 3, 3, 1, 1, 5, 1, 5, 2, 1, 4, 1, 2, 4, 4, 4, 4, 2, 2, 2, 4, 4, 4, 2, 1, 5, 5, 2, 1, 1, 1, 4, 4, 1, 4, 2, 3, 3, 3, 3, 3, 5, 4, 1, 5, 1, 4, 5, 5, 1, 1, 1, 4, 1, 2, 4, 4, 1, 2, 3, 3, 3, 3, 5, 1, 4, 2, 5, 5, 2, 1, 1, 1, 1, 3, 3, 1, 1, 2, 3, 2, 5, 4, 2, 1, 1, 2, 2, 2, 1, 3, 1, 5, 4, 1, 1, 5, 3, 3, 2, 2, 3, 1, 1, 1, 1, 2, 4, 2, 2, 5, 1, 2, 4, 2, 1, 1, 3, 2, 5, 5, 3, 1, 3, 3, 1, 4, 1, 1, 5, 5, 1, 5, 4, 1, 1, 1, 1, 2, 3, 3, 1, 2, 3, 1, 5, 1, 3, 1, 1, 3, 1, 1, 1, 1, 1, 1, 5, 1, 1, 5, 5, 2, 1, 1, 5, 2, 4, 5, 5, 1, 1, 5, 1, 5, 5, 1, 1, 3, 3, 1, 1, 3, 1]

testInput = [3, 4, 3, 1, 2]

function runSimulation(inputArray, days) {

	fishMap = fishCounter(inputArray)

	// console.log(fishMap)
	fishTotal = 0

	for (let day = 1; day <= days; day++) {
		console.log('Running simulation for day ' + day)
		fishMap = spawnFishes(fishMap)
		// console.log(fishMap)
	}

	for (let i = 0; i < 9; i++) {
		fishTotal += fishMap.get(i)
	}

	console.log(fishTotal)

}

function fishCounter(inputArray) {
	newFishes = new Map()
	for (let delay = 0; delay <= 8; delay++) {
		fishes = inputArray.filter(daysLeft => daysLeft === delay)
		newFishes.set(delay, fishes.length)
	}
	return newFishes
}

function spawnFishes(oldMap) {
	newMap = new Map()


	for (let i = 0; i < 8; i++) {
		oldFishCounter = oldMap.get(i + 1)
		newMap.set(i, oldFishCounter)
	}

	newBorns = oldMap.get(0)
	newMap.set(8, newBorns)
	currentSixes = newMap.get(6)

	newMap.set(6, (newBorns + currentSixes))
	return newMap
}

runSimulation(puzzleInput, 8081)