class numeros :
    def unidade(unidade):
            if unidade == '1':
                unidade = 'um'  
            elif unidade == '2':
                unidade = 'dois'
            elif unidade == '3':
                unidade = 'três'
            elif unidade == '4':
                unidade = 'quatro'
            elif unidade == '5':
                unidade = 'cinco'
            elif unidade == '6':
                unidade = 'seis'
            elif unidade == '7':
                unidade = 'sete'
            elif unidade == '8':
                unidade = 'oito'
            elif unidade == '9':
                unidade = 'nove'

            return unidade

    def dezenaDez(dezenaDez):           
        if dezenaDez == '1':
            dezenaDez = 'onze'
        elif dezenaDez == '2':
            dezenaDez = 'doze'
        elif dezenaDez == '3':
            dezenaDez = 'treze'
        elif dezenaDez == '4':
            dezenaDez = 'quatorze'
        elif dezenaDez == '5':
            dezenaDez = 'quinze'
        elif dezenaDez == '6':
            dezenaDez = 'dezesseis'
        elif dezenaDez == '7':
            dezenaDez = 'dezessete'
        elif dezenaDez == '8':
            dezenaDez = 'dezoito'
        elif dezenaDez == '9':
            dezenaDez = 'dezenove'
        
        return dezenaDez

    def dezena(dezena):
        if dezena == '0':
            dezena = 'dez'      
        elif dezena == '2':
            dezena = 'vinte'        
        elif dezena == '3':
            dezena = 'trinta'
        elif dezena == '4':
            dezena = 'quarenta'
        elif dezena == '5':
            dezena = 'cinquenta'
        elif dezena == '6':
            dezena = 'sessenta'
        elif dezena == '7':
            dezena = 'setenta'
        elif dezena == '8':
            dezena = 'oitenta'
        elif dezena == '9':
            dezena = 'noventa'

        return dezena

    def centena(centena):   
        if centena == '0':
            centena = 'cem' 
        elif centena == '1':
            centena = 'cento'
        elif centena == '2':
            centena = 'duzentos'
        elif centena == '3':
            centena = 'trezentos'
        elif centena == '4':
            centena = 'quatrocentos'
        elif centena == '5':
            centena = 'quinhentos'
        elif centena == '6':
            centena = 'seicentos'
        elif centena == '7':
            centena = 'setecentos'
        elif centena == '8':
            centena = 'oitocentos'
        elif centena == '9':
            centena = 'novecentos'

        return centena
