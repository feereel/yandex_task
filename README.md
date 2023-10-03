# Аварийная поставка логов
На вход принимается два парамметра FILE_PATH и URL
```
python3 sender.py FILE_PATH URL
```

# Штатная поставка логов:

Для сборки:
```
docker build . -t sender
```

Для запуска:
```
docker run --name=sender -d -v /var/log/super_mega_critical.csv:/var/log/data.csv sender
```

# Неожиданная находка:
Просмотрев все процессы я так и не нашел за что мне зацепиться, кроме процесса с PID 667 (/usr/sbin/CRON). Он имеет странную систему подпроцессов, где с помощью python скрипта открывается bash и вызывается с неизвестным мне IP 130.193.55.241 процесс. Первым делом я бы разобрался в этой структуре процессов и какие данные передаются с помощью wireshurk или tcpdump.
