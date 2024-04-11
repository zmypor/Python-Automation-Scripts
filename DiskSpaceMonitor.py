import psutil
import os
# 获取磁盘挂载点
disk_partitions = psutil.disk_partitions()
# 遍历每个挂载点
for partition in disk_partitions:
    # 获取磁盘使用情况
    disk_usage = psutil.disk_usage(partition.mountpoint)
    # 计算磁盘可用空间的百分比
    free_percent = disk_usage.free / disk_usage.total * 100
    # 如果磁盘可用空间小于10%，发送警告邮件
    if free_percent < 10:
        # 获取主机名
        hostname = os.uname()[1]
        # 构造邮件内容
        subject = f"Disk space warning on {hostname}"
        message = f"The disk {partition.device} ({partition.mountpoint}) is running out of space ({free_percent:.2f}% free)."
        # 发送邮件
        send_email(subject, message)

        import smtplib
        from email.mime.text import MIMEText
        from email.header import Header


        def send_email(subject, message):
            # 邮件发送者和接收者
            sender = 'sender@example.com'
            receiver = 'receiver@example.com'
            # 邮件主题和内容
            msg = MIMEText(message, 'plain', 'utf-8')
            msg['Subject'] = Header(subject, 'utf-8')
            # 发送邮件
            smtp = smtplib.SMTP('smtp.example.com')
            smtp.login(sender, 'password')
            smtp.sendmail(sender, receiver, msg.as_string())
            smtp.quit()