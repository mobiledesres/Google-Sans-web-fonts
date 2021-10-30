srcDir=.
dstDir=.

targetFormat="woff"

function help {
    echo "Usage: bash \"$0\" [-s srcDir] [-d dstDir] [-2] [-h]"
    echo "* If srcDir (source directory) or dstDir (destination directory) are not specified, then they are set to current working directory by default."
    echo "* Use \"-2\" for converting to woff2; default is converting to woff."
    echo "* Use \"-h\" to show this help."
}

# get arguments
while getopts "s:d:2h" OPTION; do
    case $OPTION in
    h)
        help
        exit 0
        ;;
    s)
        srcDir="$OPTARG"
        ;;
    d)
        dstDir="$OPTARG"
        ;;
    2)
        targetFormat="woff2"
        ;;
    *)
        help
        exit 1
    esac
done

srcFiles="$(find "$srcDir" -name "*.[ot]tf")"

function convertSingle {
    local srcFile="$1"

    # get temporary and destination filenames
    local tempFile=
    local dstFile=
    case $targetFormat in
    woff2)
        tempFile="${1%.*}.woff2"
        dstFile="${2%.*}.woff2"
        ;;
    *)
        tempFile="${1%.*}.woff"
        dstFile="${2%.*}.woff"
        ;;
    esac

    mkdir -p "$(dirname "$dstFile")"

    # convert
    case $targetFormat in
    woff2)
        woff2_compress "$srcFile"
        ;;
    *)
        sfnt2woff "$srcFile"
        ;;
    esac

    if [[ "$(realpath "$tempFile")" != "$(realpath "$dstFile")" ]]
    then
        mv "$tempFile" "$dstFile"
    fi
}

function convertAll {
    local IFS=$(echo -e "\n\b")
    local srcFilesArray=($srcFiles)

    for srcFile in ${srcFilesArray[@]}
    do
        # get destination filename
        local dstFile="$dstDir/${srcFile#$srcDir/}"
        case $targetFormat in
        woff2)
            dstFile="${dstFile%.*}.woff2"
            ;;
        *)
            dstFile="${dstFile%.*}.woff"
            ;;
        esac

        # convert
        convertSingle "$srcFile" "$dstFile" &
    done

    for srcFile in ${srcFilesArray[@]}
    do
        wait -f
    done
}

convertAll