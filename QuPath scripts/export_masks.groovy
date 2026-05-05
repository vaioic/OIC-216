def imageData = getCurrentImageData()

// Define output path (relative to project)
def outputDir = buildFilePath(PROJECT_BASE_DIR, 'export')
mkdirs(outputDir)
def name = GeneralTools.stripExtension(imageData.getServer().getMetadata().getName())
def path = buildFilePath(outputDir, name + "-labels.tif")

// Define how much to downsample during export (may be required for large images)
double downsample = 1

// Create an ImageServer where the pixels are derived from annotations
def imageData = getCurrentImageData()

// Define output path (relative to project)
def outputDir = buildFilePath(PROJECT_BASE_DIR, 'export')
mkdirs(outputDir)
def name = GeneralTools.stripExtension(imageData.getServer().getMetadata().getName())
def path = buildFilePath(outputDir, name + "-labels.tif")

// Define how much to downsample during export (may be required for large images)
double downsample = 1

// Create an ImageServer where the pixels are derived from annotations
def labelServer = new LabeledImageServer.Builder(imageData)
    .backgroundLabel(0, ColorTools.BLACK) // Specify background label (usually 0 or 255)
    .downsample(downsample)    // Choose server resolution; this should match the resolution at which tiles are exported
    .addLabel('Cell', 1)      // Choose output labels (the order matters!)
    .addLabel('Mitochondria', 2)
    .addLabel('Golgi body', 3)
    .addLabel('Lysosome', 4)      
    .addLabel('Secondary Lysosome', 5)
    .addLabel('ER', 6)
    .addLabel('Autophagosome', 7)      
    .addLabel('MVB', 8)
    .addLabel('Vacuole', 9)
    .addLabel('ILV', 10)      
    .addLabel('Unsure', 11)
    .addLabel('Other', 100)
    .grayscale()
    .multichannelOutput(false) // If true, each label refers to the channel of a multichannel binary image (required for multiclass probability)
    .build()

// Write the image
writeImage(labelServer, path)