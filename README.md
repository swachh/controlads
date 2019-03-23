## Control Ads
This project is aimed at blocking domains which serve ads and track users using first or third party cookies.

The way web is working today - Visitors do not have any control over scripts / JS deployed via domains. If a Visitor visits site A, she can have cookies placed on her browser from numerous websites without her consent.

To stop unwanted cookies / trackers / Javascript codes there are several Ad blockers present in the market today (Adblockers / uBlock origin etc.) 

However, to block Ads such tools intercept all requests and block the ones which serve ads. 

Swachh Ads recommends to block such ad networks on your own at DNS level by blacklisting Ad serving domains. This will stop all communications from such domains.

Ads may still appear from domain which are not added which you may also choose to whitelist. 

At the end of the day, you're in full control of what you block and what you allow without any tool intercepting your browsing.

Know more about role of hosts file [here](https://en.wikipedia.org/wiki/Hosts_(file)).

## Usage
Clone this repository and run simple python script which will append the hosts list to your system hosts file.

```bash
git clone https://github.com/swachh/controlads.git
cd controlads
sudo python appendHostsList.py /etc/hosts ./hosts
```

## Contribution
Feel free to add more domains to hosts file and send PR

## Credits
Initial hosts list picked from: [hostsfile.mine.nu](http://hostsfile.mine.nu)
