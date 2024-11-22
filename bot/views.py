from bot.service import views as sv

class HomeView(sv.TemplateView):
  text = (
    """*Welcome to EggCoin! 🥚💰*\n\n"""
    """🐣 *Get ready to hatch your coins!* 🐣\n\n"""
    """EggCoin is a fun and simple mini-game inside your Telegram. Just *tap* on the egg to start hatching your coins and see how much you can collect! 🐥 Each tap brings you closer to your goal, and the more you tap, the more coins you earn. It’s that easy!\n\n"""
    """*Here’s how it works:*\n"""
    """1. *Tap the egg* to hatch coins.\n"""
    """2. *Collect coins* and see how many you’ve earned.\n"""
    """3. *Unlock rewards* and surprise bonuses as you progress!\n\n"""
    """🎉 *Fun Features:*\n"""
    """- Simple and addictive gameplay\n"""
    """- Special bonuses and surprises when you reach milestones\n"""
    """- Compete with friends or other players in the global leaderboard!\n\n"""
    """🔔 *Get Started Now* – Start tapping, earn your EggCoins, and watch your balance grow! 💰\n\n"""
    """*Ready to hatch some eggs and collect your rewards? Tap the egg now!* 🥚✨\n"""
    )
  
class ProfileView(sv.TemplateView):
  text = (
    """*Your Profile* 👤\n\n"""
    """Welcome to your profile page! Here you can view and manage your EggCoin progress, settings, and more!\n\n"""
    """*Profile Overview:*\n"""
    """🔹 *Username*: @YourTelegramUsername\n"""
    """🔹 *EggCoins Earned*: 1500 🥚💰\n"""
    """🔹 *Coins Hatching*: 1200 🥚\n"""
    """🔹 *Current Level*: 5 🌟\n"""
    """🔹 *Next Reward*: 2000 Coins 🎁\n"""
    """🔹 *Friends Invited*: 10 👫\n\n"""
    """*Profile Settings:*\n"""
    """🔧 *Edit Profile*: Change your username, profile picture, and preferences.\n"""
    """🔧 *Notifications*: Turn notifications on/off for game updates and rewards.\n"""
    """🔧 *Privacy Settings*: Manage who can view your profile and progress.\n\n"""
    """*Achievements:*\n"""
    """🏅 *Top Coin Collector*: Earned 5000 coins!\n"""
    """🏅 *Egg Hatcher*: Hatch 1000 eggs!\n"""
    """🏅 *Leaderboard Champion*: Ranked in the top 10 on the leaderboard!\n\n"""
    """*Join the Fun*: Keep tapping to earn more coins, unlock achievements, and see your progress grow! Keep going! 🌟\n"""
    )
  
class FriendsView(sv.TemplateView):
  text = (
    """*Invite Friends and Earn Rewards* 👫🎉\n\n"""
    """Welcome to the *Friend Referral* page! Here you can invite your friends to join the EggCoin adventure and earn rewards for every friend who joins using your referral link!\n\n"""
    """*Your Referral Link*: \n"""
    """🔗 [Invite Your Friends](https://t.me/YourBotUsername?start=YourReferralCode)\n\n"""
    """*How it works:*\n"""
    """1. Share your referral link with friends.\n"""
    """2. When they join and start playing, you’ll earn *EggCoins* and unlock special rewards!\n"""
    """3. The more friends you invite, the more rewards you can earn! 🎁\n\n"""
    """*Referral Rewards:*\n"""
    """- Invite 5 friends: Get 500 EggCoins 🎉\n"""
    """- Invite 10 friends: Unlock a special bonus 🥚💰\n"""
    """- Invite 20 friends: Earn exclusive in-game rewards and achievements! 🏆\n\n"""
    """*Why Invite Friends?*\n"""
    """- Grow your network and climb the leaderboard together! 📊\n"""
    """- Unlock special bonuses and surprise gifts as you invite more players! 🎁\n"""
    """- Have fun competing with your friends and see who can earn the most coins! 🏅\n\n"""
    """*Get Started:*\n"""
    """Start sharing your referral link now and earn rewards as you invite friends to join the EggCoin fun! 🎉🥚💰\n"""
    )

class StatsView(sv.TemplateView):
  text = (
    """*EggCoin Game Statistics* 📊🥚\n\n"""
    """Welcome to the *Statistics Page*! Here you can track overall game statistics and see how the game is progressing.\n\n"""
    """*Global Stats Overview* 🌍\n"""
    """🔹 *Total Coins Collected*: 1,250,000,000 🥚💰\n"""
    """🔹 *Total Taps Made*: 50,000,000 taps 🐾\n"""
    """🔹 *Total Players*: 150,000 players 🧑‍🤝‍🧑\n"""
    """🔹 *Total Friends Invited*: 1,000,000 👫\n"""
    """🔹 *Total Rewards Unlocked*: 10,000 🎁\n\n"""
    """*Leaderboard Stats* 🏅\n"""
    """🔹 *Top Player*: @TopPlayerUsername with 500,000,000 coins 🥇\n"""
    """🔹 *Global Ranking (Top 3)*:\n"""
    """ 1. @TopPlayerUsername – 500,000,000 coins\n"""
    """ 2. @SecondPlayerUsername – 400,000,000 coins\n"""
    """ 3. @ThirdPlayerUsername – 350,000,000 coins\n\n"""
    """*Milestones & Achievements* 🎯\n"""
    """🏅 *Egg Hatcher*: 100 million eggs hatched globally! 🐣\n"""
    """🏅 *Coin Master*: 1 billion coins collected globally! 🥚💰\n"""
    """🏅 *Referral Champion*: 500,000 players invited by friends! 👫\n"""
    """🏅 *Top Tapper*: 25 billion taps made globally! 🐾\n\n"""
    """*Game Progress Breakdown* 📈\n"""
    """- *Top Players*: The top players are competing for the top spot! Who will reach 1 billion coins first? 🥇\n"""
    """- *Coins Collected*: Players around the world are rapidly collecting coins and unlocking exciting rewards! 🥚💰\n"""
    """- *Friends Invited*: Players are continuing to invite friends and grow the EggCoin community! 👫\n\n"""
    """*Keep Going!* 🚀\n"""
    """The global leaderboard is heating up, and exciting rewards are up for grabs! Keep tapping those eggs and see how you rank globally! 🥚💰\n"""
    )

class HelpView(sv.TemplateView):
  text = (
    """*EggCoin Help Guide* 📝\n\n"""
    """🐣 *What is EggCoin?*\n"""
    """EggCoin is a fun and simple mini-game where you tap an egg to hatch coins! The more you tap, the more coins you earn. It’s simple, fun, and rewarding! 💰\n\n"""
    """*How to Play:*\n"""
    """1. 🥚 *Tap the egg* to start collecting coins.\n"""
    """2. 💎 *Collect your coins* and see how much you’ve earned.\n"""
    """3. 🎁 *Unlock rewards* and surprises as you progress through the game!\n\n"""
    """🎯 *Special Features:*\n"""
    """- Simple and addictive gameplay\n"""
    """- Unlock special bonuses and milestones as you progress\n"""
    """- Compete with friends or other players on the global leaderboard!\n\n"""
    """*FAQ:*\n"""
    """- *What do I need to play?*\n"""
    """You just need to tap the egg to start collecting coins! There are no additional requirements.\n\n"""
    """- *How do I earn rewards?*\n"""
    """Keep tapping the egg to collect coins, and unlock new rewards and bonuses as you progress!\n"""
    )

class SupportView(sv.TemplateView):
  text = (
    """*Need Help? Contact Support* 🛠️💬\n\n"""
    """Welcome to the *Support Page*! If you're facing any issues or have any questions, we're here to assist you!\n\n"""
    """*Ways to Get Support:* \n"""
    """1. **FAQ** – Check out our frequently asked questions for quick answers.\n"""
    """2. **Contact Support** – If you can’t find the solution, reach out to us directly!\n"""
    """3. **Bug Reporting** – Encounter a bug? Let us know and we'll fix it ASAP.\n\n"""
    
    """*FAQ Section* 📚\n"""
    """- *How do I start collecting EggCoins?* Simply tap on the egg to start earning coins!\n"""
    """- *How can I invite friends?* Share your unique referral link to invite friends and earn rewards.\n"""
    """- *How do I edit my profile?* You can update your profile in the settings section.\n"""
    """- *What rewards can I get?* The more you tap, the more coins you earn! Reach milestones for extra rewards.\n\n"""
    
    """*Contact Us Directly* 📞\n"""
    """If you need further assistance or have any issues, please reach out to us through the following methods:\n"""
    """🔹 **Telegram**: @T1chCoder\n"""
    """🔹 **Email**: t1chcoder@eggcoin.com\n"""
    """🔹 **GitHub**: [T1chCoder](https://github.com/T1chCoder)\n\n"""
    
    """*Bug Reporting* 🐞\n"""
    """If you’ve found a bug or encountered an issue, please provide as much detail as possible so we can resolve it quickly.\n"""
    """1. Describe the issue.\n"""
    """2. Provide any steps to reproduce the issue.\n"""
    """3. Share screenshots or error messages if possible.\n\n"""
    
    """We value your feedback and will respond as quickly as possible to ensure you have the best experience with EggCoin! 🥚💬\n"""
    )