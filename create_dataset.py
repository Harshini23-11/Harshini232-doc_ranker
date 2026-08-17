from pathlib import Path

dataset_folder = Path("dataset")
dataset_folder.mkdir(exist_ok=True)

documents = {
    1: """
Agriculture is an important economic activity that provides food and raw
materials for people around the world. Modern agriculture uses improved seeds,
irrigation, fertilizers, machinery, and scientific farming techniques to
increase crop production and improve farm productivity.
""",

    2: """
Renewable energy comes from natural sources that are continuously replenished.
Solar, wind, hydroelectric, biomass, and geothermal energy are major renewable
sources. Renewable energy can reduce dependence on fossil fuels and support
cleaner electricity generation.
""",

    3: """
Solar energy uses sunlight to generate electricity or heat. Solar panels
convert sunlight into electrical energy using photovoltaic cells. Solar power
is widely used in homes, industries, farms, and large electricity generation
plants.
""",

    4: """
Wind energy converts the movement of air into useful electricity. Wind turbines
use rotating blades connected to generators. Wind farms can be built on land
or offshore where suitable wind conditions are available.
""",

    5: """
Electric vehicles use electric motors and batteries instead of conventional
internal combustion engines. They can reduce fuel consumption and tailpipe
emissions. Charging infrastructure and battery technology are important for
the growth of electric transportation.
""",

    6: """
Climate change refers to long-term changes in temperature and weather patterns.
Human activities such as burning fossil fuels and deforestation increase
greenhouse gas emissions. Reducing emissions and improving adaptation can help
address climate change.
""",

    7: """
Water conservation focuses on reducing unnecessary water consumption and
protecting freshwater resources. Rainwater harvesting, efficient irrigation,
leak prevention, recycling, and responsible household usage can help conserve
water for future generations.
""",

    8: """
Waste management involves collecting, transporting, processing, recycling, and
disposing of waste safely. Proper waste segregation can separate recyclable,
organic, and hazardous materials and reduce the amount of waste sent to
landfills.
""",

    9: """
Biotechnology uses living organisms, cells, or biological processes to develop
useful products and technologies. Applications include medicine, agriculture,
food production, genetic research, and environmental management.
""",

    10: """
Healthcare systems provide services for preventing diseases, diagnosing
conditions, treating patients, and promoting wellbeing. Hospitals, clinics,
medical professionals, medicines, diagnostic equipment, and digital health
technologies are important parts of modern healthcare.
""",

    11: """
Vaccination helps protect individuals and communities from infectious diseases.
Vaccines train the immune system to recognize specific pathogens and respond
more effectively. Immunization programs are an important part of public health.
""",

    12: """
Good nutrition provides the body with essential nutrients required for growth,
energy, and normal functioning. A balanced diet can include fruits, vegetables,
grains, proteins, healthy fats, vitamins, minerals, and adequate water.
""",

    13: """
Space exploration involves studying objects and environments beyond Earth.
Space missions use rockets, satellites, probes, and spacecraft to investigate
planets, moons, asteroids, and distant regions of space.
""",

    14: """
Astronomy is the scientific study of stars, planets, galaxies, and other
objects in the universe. Astronomers use telescopes and scientific instruments
to observe celestial bodies and understand their formation and evolution.
""",

    15: """
Satellite communication uses artificial satellites to transmit information
between distant locations. Satellites support television broadcasting, internet
services, navigation, weather observation, emergency communication, and
scientific research.
""",

    16: """
Educational technology uses digital tools to improve teaching and learning.
Interactive applications, digital classrooms, educational videos, online
assessments, and learning platforms can provide students with flexible learning
opportunities.
""",

    17: """
Online learning allows students to access educational content through the
internet. Virtual classrooms, recorded lectures, digital assignments, online
quizzes, and discussion forums can support learning from different locations.
""",

    18: """
Digital payments allow people to transfer money electronically without using
physical cash. Mobile payment applications, bank transfers, cards, and digital
wallets provide convenient methods for making financial transactions.
""",

    19: """
E-commerce enables customers to purchase products and services through digital
platforms. Online stores provide product catalogs, electronic payments, order
tracking, customer reviews, and home delivery services.
""",

    20: """
Financial technology combines technology with financial services. Fintech
applications include digital banking, mobile payments, online lending,
investment platforms, insurance technology, and automated financial services.
""",

    21: """
Tourism involves people traveling to different destinations for recreation,
business, culture, education, or other purposes. Hotels, transportation,
restaurants, attractions, travel agencies, and local communities contribute to
the tourism industry.
""",

    22: """
Transportation systems move people and goods between different locations.
Roads, railways, airports, ports, buses, trains, ships, and logistics services
form important components of modern transportation networks.
""",

    23: """
Smart cities use digital technologies and connected infrastructure to improve
urban services. Intelligent transportation, energy management, waste
collection, public safety, and digital services can improve city operations.
""",

    24: """
Disaster management involves preparing for, responding to, and recovering from
natural or human-made disasters. Emergency planning, early warning systems,
evacuation procedures, rescue operations, and recovery programs help reduce
damage and protect communities.
""",

    25: """
Weather forecasting predicts atmospheric conditions such as temperature,
rainfall, wind, and storms. Meteorologists use weather stations, satellites,
radar systems, computer models, and historical observations to prepare
forecasts.
""",

    26: """
Ocean science studies marine environments, organisms, currents, climate
interactions, and ocean resources. Research vessels, underwater instruments,
satellites, and autonomous systems help scientists understand the oceans.
""",

    27: """
Environmental protection focuses on preserving ecosystems and natural
resources. Conservation programs can protect forests, wildlife, rivers,
wetlands, and biodiversity while promoting sustainable use of natural
resources.
""",

    28: """
Food technology applies science and engineering to food production,
processing, packaging, storage, and safety. Modern food technology helps
increase shelf life, maintain quality, reduce contamination, and improve food
distribution.
""",

    29: """
Supply chain management coordinates the movement of raw materials, products,
information, and money from suppliers to customers. Inventory management,
transportation, warehousing, procurement, and demand forecasting are important
supply chain activities.
""",

    30: """
Entrepreneurship involves creating and developing new businesses or products.
Entrepreneurs identify opportunities, develop business ideas, manage resources,
take calculated risks, and create value for customers and society.
"""
}

for number, content in documents.items():
    file_path = dataset_folder / f"document{number:02d}.txt"
    file_path.write_text(content.strip(), encoding="utf-8")

print("30 documents created successfully!")
print(f"Dataset location: {dataset_folder.resolve()}")