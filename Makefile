CONVERT_EXEC := convert_to_woff_woff2.sh

TTF := TTF
WOFF := WOFF
WOFF2 := WOFF2

ttf_files := $(shell find $(TTF) -name *.ttf -exec ls --quoting-style=escape {} \;)

converted_files = $(woff_files) $(woff2_files)
woff_files := $(patsubst $(TTF)/%,$(WOFF)/%,$(ttf_files:.ttf=.woff))
woff2_files := $(patsubst $(TTF)/%,$(WOFF2)/%,$(ttf_files:.ttf=.woff2))

.PHONY: all
all: $(converted_files)

$(woff_files): $(ttf_files)
	bash $(CONVERT_EXEC) -s $(TTF) -d $(WOFF)

$(woff2_files): $(ttf_files)
	bash $(CONVERT_EXEC) -s $(TTF) -d $(WOFF2) -2

.PHONY: clean
clean:
	-rm -rfv $(WOFF) $(WOFF2)