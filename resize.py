#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Image
import glob
import sys 
import os

'''
Modo de usar:
Primeiro parêmtro: Diretório onde se encontram os arquivos *.JPG e *.jpg. Padrão: atual
Segundo parâmetro: Fator de divisão. Padrão: 2
Terceiro parâmtro: prefixo que será adicionado a fato para não sobrescrever o original. Padrão: -rzd
'''


if __name__ == '__main__':

	path = './'
	if len(sys.argv) > 1:
		path = sys.argv[1]

	ratio = float(2)		
	if len(sys.argv) > 2:
		ratio = float(sys.argv[2])
		
	prefix = '-rzd'
	if len(sys.argv) > 3:
		prefix = float(sys.argv[3])
	
	for infile in glob.glob( os.path.join(path, '*.jpg') ) + glob.glob( os.path.join(path, '*.JPG') ):
		print "current file is: " + infile
		img = Image.open(infile)
		img.resize( (lambda a: (int(a[0]/ratio), int(a[1]/ratio)))(img.size), Image.BICUBIC).save('%s%s%s' %(infile[:-4],prefix,'.jpg'))
			
