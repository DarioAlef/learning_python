#Q.01 - converta uma quantidade de tempo em dias, horas, minutos e segundos


def converter():
    tempo = int(input('\ndigite o tempo em segundos: '))
    
    dias = tempo // 86400
    horas = (tempo % 86400) // 3600
    minutos = (tempo % 3600) // 60
    segundos = tempo % 60
    
    print('\nEsse tempo equivale a', dias, 'dias', horas, 'horas', minutos, 'minutos', segundos, 'segundos\n')
    
    
    
converter()

    
