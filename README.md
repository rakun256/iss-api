# 🌌 ISS Overhead Notifier 🚀

A Python script that notifies you via email when the International Space Station (ISS) is flying over your location **at night**! Perfect for stargazers, space lovers, and romantics who want to impress their loved ones. 💌✨

---

## 📌 Features

* Checks ISS location every minute using [Open Notify API](http://api.open-notify.org/iss-now.json)
* Detects day/night based on your coordinates using [Sunrise-Sunset API](https://sunrise-sunset.org/api)
* Sends a sweet email if the ISS is above you **and** it's dark outside 🌙

---

## ⚙️ Setup Instructions

1. **Clone the repo**

```bash
git clone https://github.com/your-username/iss-overhead-notifier.git
cd iss-overhead-notifier
```

2. **Install dependencies**

This script only uses standard Python libraries, but make sure you have `requests` installed:

```bash
pip install requests
```

3. **Update your settings**

In the script, replace the placeholders:

```python
EMAIL_ADDRESS = '<YOUR_EMAIL>'
PASSWORD = '<YOUR_PASSWORD>'
MY_LOVE = 'their_email@example.com'
MY_LAT = <your_latitude>
MY_LONG = <your_longitude>
```

⚠️ Make sure to use an app password if you're using Gmail and have 2FA enabled.

4. **Run the script**

```bash
python main.py
```

It will run continuously and check every 60 seconds. 🕒

---

## 📬 Email Preview

```
Subject: Heads Up!

Iss is overhead!
```

You can customize this message to make it more romantic or exciting! 💖

---

## 🛡️ Disclaimer

* Do not hardcode sensitive credentials in public repositories. Use environment variables or `.env` files instead.
* The accuracy of the ISS position may vary slightly.

---

## 💡 Inspiration

Made with 💙 to send a smile across the stars. Inspired by love and the magic of space.

---

## 📄 License

MIT License. Use it, remix it, send some love. 🌍
