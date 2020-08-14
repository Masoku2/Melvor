from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
#import discord
#from discord.ext import commands

#client = commands.Bot(command_prefix = '!')
url = 'https://melvoridle.com/index.php?l=1'
PATH = "C:\Program Files (x86)/chromedriver.exe"
driver = webdriver.Chrome(PATH)
username = 'TestAccount123' 
password = 'TestAccount123' 

driver.get(url)
driver.maximize_window()
print(driver.title)

#driver.find_element_by_id("character-selection-login").click() 
#driver.find_element_by_id("login-username").send_keys(username)
#driver.find_element_by_id("login-password").send_keys(password)
#driver.find_element_by_id("login").click()


driver.find_element_by_id("character-select-0").click()
driver.implicitly_wait(5)
driver.find_element_by_id("start-game-btn").click()
driver.implicitly_wait(5)

#Grab GP + Combat Levels

GoldPieces = driver.find_element_by_id("nav-current-gp").text
print(GoldPieces)
driver.implicitly_wait(5)

Combat = driver.find_element_by_id("combat-level-sidebar").text
print(Combat)
driver.implicitly_wait(5)

Attack = driver.find_element_by_id("nav-skill-progress-6").text
print(Attack)
driver.implicitly_wait(5)

Strength = driver.find_element_by_id("nav-skill-progress-7").text
print(Strength)
driver.implicitly_wait(5)

Defence = driver.find_element_by_id("nav-skill-progress-8").text
print(Defence)
driver.implicitly_wait(5)

Hitpoints = driver.find_element_by_id("nav-skill-progress-9").text
print(Hitpoints)
driver.implicitly_wait(5)

Ranged = driver.find_element_by_id("nav-skill-progress-12").text
print(Ranged)
driver.implicitly_wait(5)

Magic = driver.find_element_by_id("nav-skill-progress-16").text
print(Magic)
driver.implicitly_wait(5)

Prayer = driver.find_element_by_id("nav-skill-progress-17").text
print(Prayer)
driver.implicitly_wait(5)

Slayer = driver.find_element_by_id("nav-skill-progress-18").text
print(Slayer)
driver.implicitly_wait(5)

#Skills
Woodcutting = driver.find_element_by_id("nav-skill-progress-0").text
print(Woodcutting)
driver.implicitly_wait(5)

Fishing = driver.find_element_by_id("nav-skill-progress-1").text
print(Fishing)
driver.implicitly_wait(5)

Firemaking = driver.find_element_by_id("nav-skill-progress-2").text
print(Firemaking)
driver.implicitly_wait(5)

Cooking = driver.find_element_by_id("nav-skill-progress-3").text
print(Cooking)
driver.implicitly_wait(5)

Mining = driver.find_element_by_id("nav-skill-progress-4").text
print(Mining)
driver.implicitly_wait(5)

Smithing = driver.find_element_by_id("nav-skill-progress-5").text
print(Smithing)
driver.implicitly_wait(5)

Thieving = driver.find_element_by_id("nav-skill-progress-10").text
print(Thieving)
driver.implicitly_wait(5)

Farming = driver.find_element_by_id("nav-skill-progress-11").text
print(Farming)
driver.implicitly_wait(5)

Fletching = driver.find_element_by_id("nav-skill-progress-13").text
print(Fletching)
driver.implicitly_wait(5)

Crafting = driver.find_element_by_id("nav-skill-progress-14").text
print(Crafting)
driver.implicitly_wait(5)

Runecrafting = driver.find_element_by_id("nav-skill-progress-15").text
print(Runecrafting)
driver.implicitly_wait(5)

Herblore = driver.find_element_by_id("nav-skill-progress-19").text
print(Herblore)
driver.implicitly_wait(5)

Amagic = driver.find_element_by_id("nav-skill-progress-16").text
print(Amagic)
driver.implicitly_wait(5)