# CloudConsole
A terminal/console application to monitor instances like EC2 present in environments like AWS, GCP

Monitor and Control instances via console:
```
Kshitizs-MacBook-Air:CloudConsole kbartariya$ python3 main.py 
                      ----------------------------------                       
                      |            Stopped             |                       
                      ----------------------------------                       
                      | Idx |           Name           |                       
                      ----------------------------------                       
                      |  0  |kshitiz-nginx             |                       
                      |  1  |kshitiz-q1                |                       
                      ----------------------------------                       
0) start
1) stop
2) list
3) filter
?:0
instance:1
Starting instance i-071b2252a0e87e647
                      ----------------------------------                                             ----------------------------------                       
                      |            Stopped             |                                             |            Pending             |                       
                      ----------------------------------                                             ----------------------------------                       
                      | Idx |           Name           |                                             | Idx |           Name           |                       
                      ----------------------------------                                             ----------------------------------                       
                      |  0  |kshitiz-nginx             |                                             |  1  |kshitiz-q1                |                       
                      ----------------------------------                                             ----------------------------------                       
0) start
1) stop
2) list
3) filter
?:
```
