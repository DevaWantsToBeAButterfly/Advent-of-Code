basePacket = '110100101111111000101000'

hexDictionary = new Map([
	['0000', 0],
	['0001', 1],
	['0010', 2],
	['0011', 3],
	['0100', 4],
	['0101', 5],
	['0110', 6],
	['0111', 7],
	['1000', 8],
	['1001', 9],
	['1010', 'A'],
	['1011', 'B'],
	['1100', 'C'],
	['1101', 'D'],
	['1110', 'E'],
	['1111', 'F']
])

function translateFromBinary(binary) {
	intValue = 0
	binary = binary.split("").reverse().join("")

	for (let i = 0; i < binary.length; i++) {
		asInt = parseInt(binary[i])
		intValue += (2 ** i * asInt)
	}
	return intValue
}

function checkVersion(packet) {
	versionID = '0' + packet.slice(0, 3)

	versionID = hexDictionary.get(versionID)
	packet = packet.slice(3)
	return [versionID, packet]
}

function checkType(packet) {
	typeID = '0' + packet.slice(0, 3)

	typeID = hexDictionary.get(typeID)
	packet = packet.slice(3)
	return [typeID, packet]
}

function checkLengthType(packet) {
	if (packet[0] === '0') {
		subPacketsLength = translateFromBinary(packet.slice(1, 15))
		return ('Length', subPacketsLength)
	} else {
		subPacketsCount = translateFromBinary(packet.slice(1, 11))
		return ('Count', subPacketsCount)
	}
}

function prepPacket(packet) {
	versionCheckOutput = checkVersion(packet)
	packetVersion = versionCheckOutput[0]
	packet = versionCheckOutput[1]

	typeCheckOutput = checkType(packet)
	packetType = typeCheckOutput[0]
	packet = typeCheckOutput[1]

	packetVersions.push(packetInfo[0])

	return [packetType, packet]
}

function handleLiteralPacket(packet) {
	binaryString = ''
	firstBitIndex = 0
	while (true) {
		binaryString += packet.slice(firstBitIndex + 1, firstBitIndex + 5)

		if (packet[firstBitIndex] === '0') {
			packet = packet.slice(firstBitIndex + 5)
			break
		} else {
			packet = packet.slice(firstBitIndex + 5)
			firstBitIndex += 5
		}
	}
	packetValue = translateFromBinary(binaryString)

	return (packetValue, packet)
}

function handlePacket(packet) {
	packetInfo = prepPacket(packet)
	packetType = packetInfo[0]
	packet = packetInfo[1]

	if (packetType === 4) {
		packetValue = handleLiteralPacket(packet)[0]
		foundLastSubPacket = true
	} else {
		subPacketsIdentifier = checkLengthType(packet)
		foundLastSubPacket = false
	}

	while (!foundLastSubPacket) {
		packetInfo = prepPacket(packet)
		packetType = packetInfo[0]
		packet = packetInfo[1]
		subPacketResults = handleLiteralPacket(packet)

		if (subPacketsIdentifier[0] === 'Length') {

		}
	}


}




console.log(packetVersion, packetType, packetValue)

