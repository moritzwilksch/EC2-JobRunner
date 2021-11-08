# EC2 JobRunner 🏃
Runs python script in EC2, then shuts down instance.

## Add script to crontab
```shell
# run
crontab -e

# add
@reboot /home/ec2-user/EC2-JobRunner/script.sh
```
## Circuit Breaker
- Change file `skip_shutdown.txt` to contain `yes` on main branch
