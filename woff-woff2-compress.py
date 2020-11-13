import glob, sys, subprocess as sp
from os.path import basename, dirname, abspath, relpath, normpath

sourceExts = ['ttf', 'otf']
targetExts = ['woff', 'woff2']
programs = ['sfnt2woff', 'woff2_compress']

baseDir = dirname(abspath(__file__))
if len(sys.argv) > 1:
    baseDir = sys.argv[1]
dirs = {}
for ext in (sourceExts + targetExts):
    dirs[ext] = abspath('%s/%s' % (baseDir, ext.upper()))


def get_source_font_files():
    sourceFontFiles = {}
    for sourceExt in sourceExts:
        sourceDirKey = dirs[sourceExt]
        pattern = '%s/**/*.%s' % (baseDir, sourceExt)
        sourceFontFiles[sourceDirKey] = glob.glob(pattern, recursive=True)
    return sourceFontFiles


def check_programs():
    try:
        for program in programs:
            sp.call([program], stdout=sp.DEVNULL, stderr=sp.DEVNULL)
    except OSError:
        print('Please make sure that you have both woff-tools and woff2 packages installed.')
        exit(1)


def convert(source_font_path: str, start_path: str):
    sourceFontRelPath = relpath(source_font_path, start_path)
    sourceRelPath = dirname(sourceFontRelPath)
    sourceFontFileName = basename(source_font_path)

    totalConversionCounts = len(targetExts)
    currentConversionCount = 0

    for (index, targetExt) in enumerate(targetExts):
        currentConversionCount += 1
        count = (currentConversionCount, totalConversionCounts)

        print('\nPerforming conversion: %s/%s' % count)

        targetPath = abspath('%s/%s' % (dirs[targetExt], sourceRelPath))
        sp.call(['mkdir', '-p', targetPath])

        targetFontPath = abspath('%s/%s' % (targetPath, sourceFontFileName))  # this file is still TTF/OTF
        sp.call(['cp', source_font_path, targetFontPath])
        sp.call([programs[index], targetFontPath])
        sp.call(['rm', targetFontPath])

        print('Finished conversion: %s/%s' % count)


def main():
    check_programs()
    sourceFontFiles = get_source_font_files()

    totalCounts = 0
    for (absDir, fontFiles) in sourceFontFiles.items():
        totalCounts += len(fontFiles)
    print('TOTAL: %s files' % totalCounts)

    currentCount = 0
    for (absDir, fontFiles) in sourceFontFiles.items():
        for fontFile in fontFiles:
            currentCount += 1
            count = (currentCount, totalCounts)
            print('\n\n[PROCESSING: %s/%s]' % count)
            convert(fontFile, absDir)
            print('\n[PROCESSED: %s/%s]' % count)

    exit(0)


if __name__ == '__main__':
    main()
