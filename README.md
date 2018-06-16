# KeyBot
A simple IRC bot designed to send key pressed to games. Useable for "Twitch Plays" type scenarios, though the IRC code is designed for being used on IRC. If you want a dirt-simple bot to build on, this should work. Look for similar bots for how to implement OAUTH for twitch channels. Pretty much all of us are built off of the same random python tutorials and stackexchange threads.

Pi-Bot is a similar script for running on a raspberry pi running webpi. The bot has to be ran using using sudo to access evdev (which, by the way, you might have to get using sudo pip instead of just pip because of this). I prefer to launch games like this...

```/opt/retropie/emulators/retroarch/bin/retroarch --verbose --record rtmp://live.twitch.tv/app/YOUR_TWITCH_KEY --recordconfig /home/pi/twitch.cfg -L /opt/retropie/libretrocores/lr-fceumm/fceumm_libretro.so --config /opt/retropie/configs/snes/retroarch.cfg "/home/pi/smb1.nes"```

because setting it up through retroarch is a pain. Replace cores and configs as needed but this si the basic idea of what a full runcommand expression looks like for retropie.
