Tried dictionary on md5 algorithm:
```commandline
hashcat -m 0 -a 0 -d 1 100k-passwords.txt 10m-passwords.txt
```
Output:
```commandline
Time.Started.....: Sun Apr 10 23:40:12 2022 (5 secs)
Recovered........: 81737/86688 (94.29%) Digests
Remaining........: 4951 (5.71%) Digests
```
_

With mask ?1?2?2?2?2?2?2:
```commandline
hashcat -m 0 -a 3 -d 1 100k-passwords.txt
```
Result:
```commandline
Speed.#1.........:   672.5 MH/s (18.61ms) @ Accel:1024 Loops:64 Thr:64 Vec:1
Recovered........: 81737/86688 (94.29%) Digests
```

#### Conclusion is: newer use low security passwords, generate trully random passwords, otherwise passwords can be easy recovered and you will be hackhed.
