# MoodMap Sydney
# Version 0.6 - Interactive Mood Map with Photos

screen = 0
selectedMood = ""
selectedPlace = ""

# Images
bondiImg = None
lunaImg = None
rocksImg = None
artImg = None
barangarooImg = None
chineseGardenImg = None
botanicImg = None
wendysImg = None

# Location data
places = [
    ["Royal Botanic Garden", "Stressed", 535, 340],
    ["Wendy's Secret Garden", "Stressed", 385, 205],
    ["Barangaroo Reserve", "Calm", 350, 325],
    ["Chinese Garden of Friendship", "Calm", 390, 435],
    ["Bondi Beach", "Happy", 735, 400],
    ["Luna Park", "Happy", 445, 205],
    ["Art Gallery of NSW", "Curious", 565, 385],
    ["The Rocks", "Curious", 475, 340]
]


def setup():
    global bondiImg, lunaImg, rocksImg, artImg
    global barangarooImg, chineseGardenImg, botanicImg, wendysImg

    size(900, 600)
    rectMode(CENTER)

    # Load images using exact filenames
    bondiImg = loadImage("bondi.jpg")
    lunaImg = loadImage("luna2.jpeg")
    rocksImg = loadImage("rocks.jpg")
    artImg = loadImage("artgallery2.jpeg")
    barangarooImg = loadImage("barangaroo.jpeg")
    chineseGardenImg = loadImage("chinesegarden2.jpg")
    botanicImg = loadImage("botanicgarden2.jpeg")
    wendysImg = loadImage("wendysgarden2.jpeg")

    # Check whether images loaded successfully
    print("Bondi:", bondiImg)
    print("Luna:", lunaImg)
    print("Rocks:", rocksImg)
    print("Art Gallery:", artImg)
    print("Barangaroo:", barangarooImg)
    print("Chinese Garden:", chineseGardenImg)
    print("Botanic Garden:", botanicImg)
    print("Wendys Garden:", wendysImg)


def draw():
    background(245, 240, 255)

    if screen == 0:
        drawWelcome()

    elif screen == 1:
        drawMood()

    elif screen == 2:
        drawMap()

    elif screen == 3:
        drawDetail()


# --------------------------------
# Welcome Page
# --------------------------------

def drawWelcome():
    textAlign(CENTER)

    fill(80, 55, 120)
    textSize(55)
    text("MoodMap Sydney", width/2, 220)

    fill(100)
    textSize(20)
    text("Navigate Sydney by how you feel", width/2, 265)

    noStroke()
    fill(255, 220, 90)
    rect(width/2, 360, 200, 65, 15)

    fill(60)
    textSize(22)
    text("START", width/2, 368)


# --------------------------------
# Mood Selection Page
# --------------------------------

def drawMood():
    textAlign(CENTER)

    fill(80, 55, 120)
    textSize(38)
    text("How are you feeling today?", width/2, 100)

    fill(100)
    textSize(17)
    text("Choose the mood that feels closest to you.", width/2, 140)

    # Stressed
    if selectedMood == "Stressed":
        stroke(80, 55, 120)
        strokeWeight(5)
    else:
        noStroke()

    fill(255, 190, 190)
    rect(250, 260, 220, 90, 20)

    noStroke()
    fill(60)
    textSize(20)
    text("Stressed", 250, 267)

    # Calm
    if selectedMood == "Calm":
        stroke(80, 55, 120)
        strokeWeight(5)
    else:
        noStroke()

    fill(190, 220, 255)
    rect(650, 260, 220, 90, 20)

    noStroke()
    fill(60)
    text("Calm", 650, 267)

    # Happy
    if selectedMood == "Happy":
        stroke(80, 55, 120)
        strokeWeight(5)
    else:
        noStroke()

    fill(255, 230, 150)
    rect(250, 400, 220, 90, 20)

    noStroke()
    fill(60)
    text("Happy", 250, 407)

    # Curious
    if selectedMood == "Curious":
        stroke(80, 55, 120)
        strokeWeight(5)
    else:
        noStroke()

    fill(200, 230, 190)
    rect(650, 400, 220, 90, 20)

    noStroke()
    fill(60)
    text("Curious", 650, 407)

    # Next button
    if selectedMood != "":
        fill(80)
        textSize(16)
        text("You selected: " + selectedMood, width/2, 490)

        noStroke()
        fill(80, 55, 120)
        rect(width/2, 540, 160, 50, 15)

        fill(255)
        textSize(18)
        text("NEXT", width/2, 546)


# --------------------------------
# Sydney Map
# --------------------------------

def drawSydneyMap():

    # Different colours for different moods
    if selectedMood == "Stressed":
        waterColour = color(220, 195, 205)
        northColour = color(240, 218, 220)
        cityColour = color(235, 220, 215)

    elif selectedMood == "Calm":
        waterColour = color(180, 215, 232)
        northColour = color(226, 232, 220)
        cityColour = color(230, 225, 215)

    elif selectedMood == "Happy":
        waterColour = color(185, 220, 235)
        northColour = color(250, 235, 185)
        cityColour = color(250, 220, 185)

    else:
        waterColour = color(205, 200, 230)
        northColour = color(220, 230, 205)
        cityColour = color(230, 220, 235)

    # Map background
    noStroke()
    fill(cityColour)
    rect(width/2, 330, 700, 360, 25)

    # North Shore
    fill(northColour)
    beginShape()
    vertex(100, 150)
    vertex(800, 150)
    vertex(800, 245)
    vertex(700, 250)
    vertex(620, 255)
    vertex(540, 250)
    vertex(465, 260)
    vertex(400, 250)
    vertex(330, 260)
    vertex(250, 250)
    vertex(170, 260)
    vertex(100, 250)
    endShape(CLOSE)

    # Sydney Harbour
    fill(waterColour)
    beginShape()
    vertex(100, 250)
    vertex(170, 260)
    vertex(250, 250)
    vertex(330, 260)
    vertex(400, 250)
    vertex(465, 260)
    vertex(540, 250)
    vertex(620, 255)
    vertex(700, 250)
    vertex(800, 245)

    vertex(800, 330)
    vertex(720, 345)
    vertex(650, 335)
    vertex(580, 350)
    vertex(520, 345)
    vertex(455, 350)
    vertex(400, 360)
    vertex(340, 350)
    vertex(280, 365)
    vertex(220, 350)
    vertex(160, 365)
    vertex(100, 355)
    endShape(CLOSE)

    # Darling Harbour
    fill(waterColour)
    beginShape()
    vertex(320, 350)
    vertex(375, 355)
    vertex(365, 445)
    vertex(345, 465)
    endShape(CLOSE)

    # Eastern inlet
    fill(waterColour)
    beginShape()
    vertex(505, 345)
    vertex(540, 345)
    vertex(530, 395)
    endShape(CLOSE)

    # City lines
    stroke(205, 200, 195)
    strokeWeight(1)

    line(170, 415, 280, 415)
    line(190, 450, 300, 450)
    line(580, 425, 690, 425)
    line(600, 460, 710, 460)

    # Sydney Harbour Bridge
    stroke(95)
    strokeWeight(4)
    noFill()

    line(455, 255, 455, 355)
    arc(455, 305, 85, 100, HALF_PI, PI + HALF_PI)

    strokeWeight(2)
    line(425, 270, 455, 270)
    line(415, 290, 455, 290)
    line(413, 310, 455, 310)
    line(420, 330, 455, 330)

    strokeWeight(4)
    line(445, 255, 465, 255)
    line(445, 355, 465, 355)

    # Labels
    noStroke()
    textAlign(CENTER)

    fill(110, 140, 155)
    textSize(11)
    text("SYDNEY HARBOUR", 630, 300)

    fill(130)
    text("CBD", 490, 430)


# --------------------------------
# Interactive Location Markers
# --------------------------------

def drawMarker(name, x, y):

    d = dist(mouseX, mouseY, x, y)

    # Hover effect
    if d < 25:
        noStroke()
        fill(255, 220, 90)
        ellipse(x, y, 38, 38)

        fill(80, 55, 120)
        ellipse(x, y, 12, 12)

    else:
        noStroke()
        fill(255)
        ellipse(x, y, 30, 30)

        fill(80, 55, 120)
        ellipse(x, y, 18, 18)

    # Location name
    fill(60)
    textSize(14)
    textAlign(CENTER)

    if name == "Luna Park" or name == "Wendy's Secret Garden":
        text(name, x, y - 25)
    else:
        text(name, x, y + 32)

    # Hover message
    if d < 25:
        fill(100)
        textSize(12)

        if name == "Luna Park" or name == "Wendy's Secret Garden":
            text("Click to explore", x, y - 43)
        else:
            text("Click to explore", x, y + 50)


# --------------------------------
# Map Page
# --------------------------------

def drawMap():
    textAlign(CENTER)

    fill(80, 55, 120)
    textSize(32)
    text("Your " + selectedMood + " Sydney", width/2, 65)

    fill(100)
    textSize(16)
    text("Move your mouse over a location to explore.", width/2, 100)

    drawSydneyMap()

    # Show only locations matching selected mood
    for place in places:
        name = place[0]
        mood = place[1]
        x = place[2]
        y = place[3]

        if mood == selectedMood:
            drawMarker(name, x, y)

    # Change mood button
    noStroke()
    fill(80, 55, 120)
    rect(width/2, 555, 180, 45, 15)

    fill(255)
    textSize(16)
    text("CHANGE MOOD", width/2, 560)


# --------------------------------
# Location Detail Page
# --------------------------------

def drawDetail():
    textAlign(CENTER)

    fill(100)
    textSize(14)
    text("MOODMAP RECOMMENDS", width/2, 45)

    fill(80, 55, 120)
    textSize(30)
    text(selectedPlace, width/2, 82)

    # Select location photo
    photo = None

    if selectedPlace == "Bondi Beach":
        photo = bondiImg

    elif selectedPlace == "Luna Park":
        photo = lunaImg

    elif selectedPlace == "The Rocks":
        photo = rocksImg

    elif selectedPlace == "Art Gallery of NSW":
        photo = artImg

    elif selectedPlace == "Barangaroo Reserve":
        photo = barangarooImg

    elif selectedPlace == "Chinese Garden of Friendship":
        photo = chineseGardenImg

    elif selectedPlace == "Royal Botanic Garden":
        photo = botanicImg

    elif selectedPlace == "Wendy's Secret Garden":
        photo = wendysImg

    # Display photo
    if photo != None:
        image(photo, 250, 105, 400, 220)
    else:
        fill(100)
        textSize(16)
        text("Photo unavailable", width/2, 220)

    # Mood recommendation
    fill(100)
    textSize(14)
    text("Recommended for:", width/2, 365)

    fill(80, 55, 120)
    textSize(22)
    text(selectedMood, width/2, 395)

    # Description
    fill(80)
    textSize(15)
    text(getDescription(selectedPlace), width/2, 435)

    # Back button
    noStroke()
    fill(80, 55, 120)
    rect(width/2, 515, 190, 50, 15)

    fill(255)
    textSize(16)
    text("BACK TO MAP", width/2, 521)


# --------------------------------
# Location Descriptions
# --------------------------------

def getDescription(name):

    if name == "Royal Botanic Garden":
        return "A green space to slow down and take a break."

    elif name == "Wendy's Secret Garden":
        return "A quiet garden for stepping away from a busy day."

    elif name == "Barangaroo Reserve":
        return "A waterfront space for walking, resting and slowing down."

    elif name == "Chinese Garden of Friendship":
        return "A peaceful garden for a slower moment in the city."

    elif name == "Bondi Beach":
        return "A lively coastal space for sunshine, movement and energy."

    elif name == "Luna Park":
        return "A playful place for colour, movement and fun."

    elif name == "Art Gallery of NSW":
        return "A place to explore art, ideas and something unfamiliar."

    elif name == "The Rocks":
        return "Explore historic streets, small details and hidden stories."

    return "Explore this Sydney location."


# --------------------------------
# Mouse Interaction
# --------------------------------

def mousePressed():
    global screen
    global selectedMood
    global selectedPlace

    # Welcome page
    if screen == 0:

        if 350 < mouseX < 550 and 327 < mouseY < 393:
            screen = 1

    # Mood selection
    elif screen == 1:

        if 140 < mouseX < 360 and 215 < mouseY < 305:
            selectedMood = "Stressed"

        elif 540 < mouseX < 760 and 215 < mouseY < 305:
            selectedMood = "Calm"

        elif 140 < mouseX < 360 and 355 < mouseY < 445:
            selectedMood = "Happy"

        elif 540 < mouseX < 760 and 355 < mouseY < 445:
            selectedMood = "Curious"

        elif 370 < mouseX < 530 and 515 < mouseY < 565:
            if selectedMood != "":
                screen = 2

    # Map interaction
    elif screen == 2:

        for place in places:
            name = place[0]
            mood = place[1]
            x = place[2]
            y = place[3]

            if mood == selectedMood:

                d = dist(mouseX, mouseY, x, y)

                if d < 25:
                    selectedPlace = name
                    screen = 3
                    break

        # Change mood
        if screen == 2:
            if 360 < mouseX < 540 and 532 < mouseY < 578:
                screen = 1

    # Detail page
    elif screen == 3:

        if 355 < mouseX < 545 and 490 < mouseY < 540:
            screen = 2
            
