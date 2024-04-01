# CloudConsole
A terminal/console application to monitor instances like EC2 present in environments like AWS, GCP

Monitor and Control instances via console:
```
                                                                          eu-north-1                                                                          
                                                                          ----------                                                                          
                    ---------------------------------------                    
                    |               Stopped               |                    
                    ---------------------------------------                    
                    | Idx |             Name              |                    
                    ---------------------------------------                    
                    |  0  |ahmed-geoforwarder-1           |                    
                    |  1  |ahmed-forwarder-stress-test-1  |                    
                    |  2  |ahmed-forwarder-test           |                    
                    |  3  |ahmed-forwarder-test-new       |                    
                    |  4  |ahmed-forwarder-qqqqq-server   |                    
                    |  5  |ahmed-forwarder-qqqqq-server-2 |                    
                    |  6  |ahmed-geoforwarder-new-2       |                    
                    |  7  |ahmed-geoforwarder-new-1       |                    
                    |  8  |ahmed-forwarder-stress-test-2  |                    
                    |  9  |ahmed-forwarder-qqqqq-server-3 |                    
                    | 10  |ahmed-forwarder-stress-test-3  |                    
                    | 11  |ahmed-forwarder-test-new-2     |                    
                    | 12  |ahmed-forwarder-stress-test-5  |                    
                    | 13  |ahmed-forwarder-qqqqq-server-5 |                    
                    | 14  |ahmed-forwarder-stress-test-4  |                    
                    | 15  |ahmed-forwarder-qqqqq-server-4 |                    
                    | 16  |ahmed-forwarder-qqqqq-server-1 |                    
                    ---------------------------------------                    
                                                                          us-west-1                                                                           
                                                                          ---------                                                                           
                        ------------------------------                         
                        |          Running           |                         
                        ------------------------------                         
                        | Idx |         Name         |                         
                        ------------------------------                         
                        |  0  |tf-forwarder-server-1 |                         
                        |  1  |tf-forwarder-server-2 |                         
                        ------------------------------                         

Filter: *forwarder*

0) start
1) stop
2) list
3) filter
4) configure
eu-north-1:
```
Some cool features:
1. Displays instances from multiple regions on a single console.
2. start/stop multiple instances simply by giving instance index in format e.g.: 0-7,8,10-13
3. Filter instances using a regular expression.
4. All configuration is stored in home directory and persistent.

Comming soon!:
1. Display multiple columns like PublicIP, InstanceID etc. based on user's configuration.
2. Support for GCP.
