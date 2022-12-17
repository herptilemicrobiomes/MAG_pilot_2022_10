library(tidyverse)
library(dplyr)
library(cowplot)
uhm91 <- read_tsv("UHM91.bin_depth.tsv")
uhm91.fil <- uhm91 %>% filter(MEAN_DEPTH < 1000) %>% arrange(MEAN_DEPTH)
p <- ggplot(uhm91.fil, aes(x=BIN,y=MEAN_DEPTH)) +  geom_bar(stat = "identity") + coord_flip() +
    scale_fill_hue(c = 40) + theme_cowplot(12)
p

