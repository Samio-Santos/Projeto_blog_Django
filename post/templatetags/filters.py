from django import template

register = template.Library()

@register.filter(name='plural_comentarios')
def plural_comentarios(num_comentarios):

    try:
        num_comentarios = int(num_comentarios)
        if num_comentarios == 0:
            return f'Nenhum comentário'

        elif num_comentarios == 1:
            return f'{num_comentarios} Comentário'
            
        else:
            return f'{num_comentarios} Comentários'

    except:
        return f'{num_comentarios} Comentários'

@register.filter(name='plural_resposta')
def plural_resposta(num_resp):
    try:
        num_resp = int(num_resp)
        if num_resp == 1:
            return f'Ver {num_resp} resposta'
        
        elif num_resp > 1:
            return f'Ver {num_resp} respostas'
    except:
        return f'{num_resp} respostas'


