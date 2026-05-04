// The purpose of this script is to ensure that we have uniform class names and colors.
Platform.runLater {
    // This creates classis if they were not previously available
    getQuPath().getAvailablePathClasses().setAll(
        getPathClass(null, makeRGB(187, 187, 187)), // Important to keep this!
        getPathClass('Mitochondria', makeRGB(0, 144, 178)), 
        getPathClass('Golgi body', makeRGB(230, 159, 0)),
        getPathClass('Cell', makeRGB(0, 158, 115)),
        getPathClass('Lysosome', makeRGB(213, 94, 0)),
        getPathClass('Secondary Lysosome', makeRGB(191, 255, 0)),
        getPathClass('ER', makeRGB(240, 228, 66)),
        getPathClass('Autophagosome', makeRGB(128, 128, 0)),
        getPathClass('MVB', makeRGB(204, 121, 167)),
        getPathClass('Vacuole', makeRGB(255, 0, 127)),
        getPathClass('ILV', makeRGB(255, 255, 255)),
        getPathClass('Unsure', makeRGB(0, 255, 255))
    )
    
    // This sets their colors if the class was previously created
    getPathClass('None').setColor(makeRGB(187, 187, 187)) // Important to keep this!
    getPathClass('Mitochondria').setColor(makeRGB(0, 144, 178))
    getPathClass('Golgi body').setColor(makeRGB(230, 159, 0))
    getPathClass('Cell').setColor(makeRGB(0, 158, 115))
    getPathClass('Lysosome').setColor(makeRGB(213, 94, 0))
    getPathClass('ER').setColor(makeRGB(143, 0, 255))
    getPathClass('Autophagosome').setColor(makeRGB(128, 128, 0))
    getPathClass('MVB').setColor(makeRGB(204, 121, 167))
    getPathClass('Secondary Lysosome').setColor(makeRGB(191, 255, 0))
    getPathClass('Vacuole').setColor(makeRGB(255, 0, 127))
    getPathClass('ILV').setColor(makeRGB(255, 255, 255))
    getPathClass('Unsure').setColor(makeRGB(0, 255, 255))
}

