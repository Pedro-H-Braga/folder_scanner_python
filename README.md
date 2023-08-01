# Varredura de duas pasta para achar a diferença entre ela (se houve modificação entre duas pastas 'irmãs')

## Motivação do projeto
Projeto desenvolvido para diminuir o trabalho de verificação manual das pastas dos clientes. Sendo necessário escolher duas pastas "irmãs" que você queira fazer a verificação, gerando um arquivo texto que terá as diferenças entre elas. 

## Exemplos de uso 

Um exemplo de uso desse script é quando se tem uma pasta sincronizada com o google drive que está no computador X e outra pasta que é a mesma porém não está sincronizada e está no computador Y, usando o script para saber se tem coisas diferentes entre elas, gerará o resultado em .txt.

## Requisitos para rodar o projeto
Projeto criado em Python utilizando as bibliotecas OS e glob para verificação das movimentações das pastas dos clientes, e PySimpleGUI para interface.

# REQUERIMENTOS DE BIBLIOTECAS NO ARQUIVO requirements.txt
