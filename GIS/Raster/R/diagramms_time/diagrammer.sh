#!/usr/bin/env Rscript

data <- read.table(file="data.txt", 
                   header = T,                 # заголовки колонок в первой строке
                   sep = "\t",                 # разделитель между колонками - табулятор
                   dec = ".")                  # разделитель целой и дробной части - .

# Строим график в png
png(filename = "picture.png",
    width = 700, height = 500, pointsize = 14,
    family = "times", bg = "white",
    antialias = c("default", "none", "gray", "subpixel"))
plot(data$YEAR,data$VALUE, bty="L", type="h", lwd=3, main="НАЗВАНИЕ ГРАФИКА",
     xlab = "Год", ylab = "Концентрация", col=data$PERIOD)
dev.off() 

