# Virtual DE1 SOC

- Property of Prof Manton / University of Melbourne (Ask them for the license if any) 
 

## Dependencies 

Modelsim

Python 3.8.2

Dependencies  
- keyboard
`python -m pip install keyboard`
https://pypi.org/project/keyboard/

Future dependencies
- ncurses
`python -m pip install windows-curses`

## Notes

On linux systems keyboard requires root access.
To get python the the class VM please follow these steps:

```
sudo su
sudo yum update
sudo yum install centos-release-scl
sudo yum --disablerepo="*" --enablerepo="centos-sclo-rh" list *python3*
sudo yum install rh-python36
scl enable rh-python36 bash
python -V
sudo echo 'scl enable rh-python36 bash' >> ~/.bash_profile
```


![Virtual DE1 SoC](/images/screen.png)

## Todo

[ ] Fix the vsim fatal error on close

[x] Fix the linux modelsim issue

[ ] Add the linux make file for ELEN30010 virtual box

[ ] Add the linux setup sh file for ELEN30010 virtual box

[x] Add the target path 

[ ] Add the lib check

[ ] Add the list modules option

[x] Add vlog result page display

[x] Add the main loop dealy 

[x] Add key record loop 

[ ] Add auto updating config input length
