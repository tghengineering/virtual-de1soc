# Virtual DE1 SOC

- Property of Prof Manton / University of Melbourne (Ask them for the license if any) 
 

## Dependencies 

Modelsim

Python 3.8.2

Dependencies  
- keyboard
`python -m pip install keyboard`


Future dependencies
- ncurses
`python -m pip install windows-curses`

## Notes

To get python the the class VM please follow these steps:

```
sudo yum update
sudo yum install centos-release-scl
sudo yum --disablerepo="*" --enablerepo="centos-sclo-rh" list *python3*
sudo yum install rh-python36
scl enable rh-python36 bash
python -V
sudo echo 'scl enable rh-python36 bash' >> ~/.bash_profile
```


![Virtual DE1 SoC](/images/screen.png)
