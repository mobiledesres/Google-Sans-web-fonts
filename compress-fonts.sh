sourceFileType=*.ttf

ttfPath=TTF
woffPath=WOFF
woff2Path=WOFF2

compress()
{
  sourcePath=$1
  targetPath=$2
  program=$3
  cp "$sourcePath/"*.ttf "$targetPath"
  for i in "$targetPath"/*.ttf
  do
    echo "\nPROCESSING FILE: $i"
    "$program" "$i"
  done
  rm "$targetPath"/*.ttf
}

compress "$ttfPath" "$woffPath" sfnt2woff
compress "$ttfPath" "$woff2Path" woff2_compress
