---
title: Windows 10 update Error
date: 2025-01-21
draft: false
tags:
  - galvin
  - blog
---
# How to fix a Blue Screen after Windows 10 Update

## What is a Blue Screen after Windows 10 Update?
- A Blue Screen after Windows 10 Update, is where Windows is trying to complete implementing the updates, but gets stuck in the process. You might see a screen much like the image below.

![Image Description](/images/Pasted%20image%2020250121234655.png)

Today I came across a laptop that was stuck in a after Windows 10 Update where no amount of restarting, or rebooting, you would come back to the same point.
# How I fixed the issue

The way to fix this issue was actually quite simple and I will help you through the process.

- The first thing you need to do is turn the computer off and on several times, before you get to the loading screen. This should start Windows diagnosing the computer and preparing Automatic Repair.

![Image Description](/images/Pasted%20image%2020250122075431.png)
![Image Description](/images/Pasted%20image%2020250122075757.png)

- If you get the following screen, click on Advanced options.

![Image Description](/images/Pasted%20image%2020250122080132.png)
- When you get to this screen you need to click on Troubleshoot to enter the Advanced Options menu.
![Image Description](/images/Pasted%20image%2020250122081229.png)
- From here you are going to click on Startup Settings, then click on Restart.
![Image Description](/images/Pasted%20image%2020250122081035.png)

![Image Description](/images/Pasted%20image%2020250122081241.png)
- Now that your computer has Restarted to this menu, you need to press 4 on your keyboard to enter Safe Mode.
![Image Description](/images/Pasted%20image%2020250122081254.png)
- From here you will see a similar update screen, but it will be removing the update and cleaning up the install.
- After the update Blue Screen Windows will launch in Safe Mode.
- Once the system has loaded, you can Restart your computer again and it should load correctly.
