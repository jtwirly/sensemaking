# -----------------------------------------------
#  14. New and Discontinued Subjects:
# 
#  Identify subjects that were offered in 
#  1996 but no longer exist in 2024, as 
#  well as new subjects introduced in 2024. 
#  Explore possible reasons for these changes.
# -----------------------------------------------


import json

with open('10_mit_1996.json') as f:
    data_1996 = json.load(f)

with open('11_mit_2024.json') as f:  
    data_2024 = json.load(f)

subjects_1996 = {d['course_code']: d['course_title'] for d in data_1996}
subjects_2024 = {d['course_code']: d['course_title'] for d in data_2024}

discontinued_codes = set(subjects_1996.keys()) - set(subjects_2024.keys())
new_codes = set(subjects_2024.keys()) - set(subjects_1996.keys())

with open('new_and_discontinued_subjects.txt', 'w') as f:
    f.write("Subjects discontinued between 1996 and 2024:\n")
    for code in discontinued_codes:
        f.write(f"{code}: {subjects_1996[code]}\n")
        
    f.write("\nNew subjects introduced by 2024:\n")    
    for code in new_codes:
        f.write(f"{code}: {subjects_2024[code]}\n")
        
    f.write("""
Possible reasons for changes in MIT's course catalog:
- Evolving fields and research areas (e.g. new tech)
- Interdisciplinary programs and combined majors  
- Revisions to core curriculum and requirements
- Updated course numbering schemes
- Response to student interest and enrollment trends  
""")

print("Results written to new_and_discontinued_subjects.txt")

"""
Subjects discontinued between 1996 and 2024:
1.52: Design of Concrete Structures
3.63: Ceramic Processes
3.062: Polymer Chemistry
1.482: Studies in Construction Engineering
16.97: Advanced Engineering Internship
13.14J: Structural Mechanics in Nuclear
2.882: Principles of Axiomatic Design
15.036: Modern Econometrics for
3.951J: Deformation and Fracture of
15.237: Business Organization and
13.951: Transport, Fate, and Effects of
4.165: Architectural Design in Islamic
3.40J: Physical Metallurgy
16.382: Lasers and Optics for
18.312: Algebraic Combinatorics
8.325: Relativistic Quantum Field Theory Il
15.312: Managerial Decision Making
12.813: Atmospheric Convection
11.521: Computer-Based Analysis for Public
10.547J: Health Technology
6.338J: Parallel Scientific Computing
11.301J: Urban Design and Development
3.989: Materials in Ancient Societies: Metals
2.981: Low-Temperature Refrigeration
5.56: Special Topics in Organic
17.241: Introduction to the American
6.851: Theory of Algorithms
11.486J: Economic Institutions and Growth
2.30: Mechanical Behavior of Materials
6.373: Computer-Aided Design of Integrated
15.761: Operations Management
14.41: Public Economics
15.664: Management of Human
13.412: Principles of Naval Ship Design
15.778: Managing Services: Concepts,
14.295J: Theory of Collective Choice:
3.64: Special Problems in Ceramics
6.241: Dynamic Systems and Control
21.ThT: Humanities Pre-Thesis Tutorial
14.286J: Health Economics Seminar
1.212: An Introduction to Intelligent
11.379J: Transportation and Government —
13.49: Maneuvering and Control of Surface
24.408: Kant
15.351: Introduction to Technological
13.016: Introduction to Geometric Modeling
15.427J: Real Estate Capital Markets
5.913: Seminar in Organic Chemistry
2.942: Entrepreneurship
18.076: Advanced Calculus for Engineers Il
17.842: Quantitative Research in Political
11.329J: User Needs Programming
16.951: Entrepreneurship
1.361: Advanced Soil Mechanics
3.271: Structure of Materials
15.827: Consumer Marketing
5.23J: Atmospheric Chemistry
11.426: Massachusetts Economy and
13.011: Ocean Science and Technology
1.543: Planning and Design of Structural
4.42J: Fundamentals of Energy in Buildings,
8.512: Theory of Solids I!
4.638: Advanced Study in Renaissance
12.459: Sedimentary and Surficial Geology
6.013: Electromagnetic Fields and Energy
24.171: Introduction to Phenomenology
6.451: Principles of Communication
1.697J: Oceanographic Systems |
14.473: Income Distribution, Growth, and
17.432: Causes of War: Theory and Method
12.745: Ore Deposition at Submarine Ridge
17.916: Junior Colloquium in Political Science and Public Affairs,12, HASS.
44.THU: Thesis (15 units)*
17.548: Chinese Politics and Political
2.THU: Undergraduate Independent Study
1.72: Groundwater Hydrology
12.102: Environmental Earth Science
4.43: Architectural Acoustics
18.421: Algorithmic Algebra and Number
48.700: Linear Algebra, 12; 18.02"
3.912: Polymer Processing
6.021J: by permission of instructor. 2 Engineer-
15.979: Seminar in Management Il
6.863J: Natural Language and the Computer
17.913: Pre-thesis Reading Seminar
1.133: M.Eng. Concepts of Engineering
10.971: Seminar in Fluid Mechanics and
2.034: Nonlinear Dynamics
2.56: Conduction and Change of Phase Heat
11.40: Introduction to Housing and
9.68: Affect: Biological, Psychological, and
22.93: Teaching Experience in Nuclear
1.731: Water Resource Systems
1.259J: Transit Management
10.988: Synthesis and Surface Chemistry of
13.863: Ocean Seismo-Acoustics
22.212: Special Problems in Advanced
12.603: Solar System Dynamics
13.020: Introduction to Fluid Mechanics for
17.523: Ethnicity and Race in World Politics
10.911: Independent Research Problem
18.385: Nonlinear Dynamics and Chaos
2.672: Project Laboratory
15.837: Special Seminar in Marketing
11.364: International Environmental
4.661: Theory and Method in the Study of
43.014: Marine Structures and Materials, 12; 2.001, 18.03
13.92: Marine Policy
4.322: Introduction to Sculpture.
3.901: Special Problems in Polymer Science
10.985: Seminar in Combustion Chemistry
1.131: Mathematical Techniques and
2.795J: Fields, Forces, and Flows:
18.248: String Theory
6.728: Applied Quantum and Statistical
8.292J: Fluid Physics
12.811: Tropical Meteorology
2.192: Engineering Systems Analysis
11.467J: Property Rights Under Transition
15.940: Environment and Product/Process
12.510: Elements of Seismology
6.688J: Strategic Analysis for
1.50: Structural Engineering
1.208J: Transportation and Logistics
16.251: Structural Design for Longevity
18.457: Sampling, Simulation, and
8.962: General Relativity
17.512: Political Culture and Democracy
6.374: Analysis and Design of Digital
15.950: Special Studies in Management
4.651: 20th-Century Art
6.301: Solid-State Circuits
18.307: Methods of Applied
22.39: Nuclear Reactor Operations and
18.966: Geometry of Manifolds Canberepeatedforcredit,
3.069: Ceramics Processing
4.291: Special Problems in Architecture
4.643J: Modern Art and Sexuality
24.728: Topics in Semantics
3.911: Professional Development for
17.301J: Science, Technology, and
22.843: Technology, Productivity, and
14.771: Development Economics:
5.92: Seminar in Environmental Chemistry
8.242: Quantum Electronics and Laser
17.423: Causes and Prevention of War
15.762: Operations Management Models
13.871: Wave Scattering by Rough Surfaces
14.63: Labor in Industrial Society
3.62: Defect Thermodynamics and Solid
6.635: Topics in Electromagnetism
2.25: Advanced Fluid Mechanics
4.607: Thinking About Architecture: In
6.672: Continuum Electromechanics II
1.56J: Structural Mechanics in Nuclear
4.378: Special Problems in Environmental
14.692J: Research Seminar in Industrial
14.102: Mathematics for Economists
15.814: Marketing Management
4.174: Design Workshop: School and
11.526J: Logistical and Transportation
1.42J: Fundamentals of Energy in Buildings
6.845: Parallel Processing: VLSI and
15.082: Network Optimization
11.026J: Downtown
2.280: Fundamentals and Modeling in
17.534: Domestic Politics of Western
10.ThG: Graduate Thesis
17.514: Philosophy of Science and the
17.116: Cultural Perspectives on Politics
4.289: Preparation for Architecture
6.023J: Quantitative Physiology: Sensory
1.128J: Computational Geometry
12.820: Instability and Turbulence in
1.711: Engineering Hydrology
6.910: Special Studies in Electrical
17.261: Congress and the Policy Process
15.410: or 15.411 or 15.414 or 15.415,
15.771J: Case Studies in Logistics and
22.67: Principles of Plasma Diagnostics
22.093: Special Topics in Nuclear
12.708: Special Topics in Paleoceanography
2.UR: Undergraduate Research in
18.410J: Introduction to Algorithms
9.70: Social Psychology
12.215: Modern Navigation
6.003: Signals and Systems
22.069: Undergraduate Plasma Laboratory
4.220: Urban Housing: Paris, London,
16.983: Advanced Special Subject
24.801: Philosophy of Mathematics
13.410: Introduction to Naval Architecture
6.042J: Mathematics for Computer Science
9.611J: Natural Language and the Computer
9.14: Development and Structure of the
1.258J: Public Transportation Service and
6.336: Introduction to Numerical
11.902: Research Seminar: Topics in Urban
4.453: Building Technology in Real Estate
4.609: Seminar in the History of Art and
13.771: Engineering Internship
14.472: Public Economics Il
14.74: Economic Growth and Development
12.746: Marine Organic Geochemistry
17.268: The President
15.875: Applications of System
1.271: Research Seminar in Transportation
14.573J: The Economics of Cities and
17.264: Dynamics of Electoral Politics
1.UR: Research in Civil and Environmental
11.450: American Living Standards and
18.466: Mathematical Statistics
14.582: International Economics Il
12.866: Theory of the General Circulation of
12.482: Advanced Field Geology Il
5.77J: Topics in Metabolic Biochemistry
15.566: Information Technology as an
17.176J: Industrial Development and Policy
11.233: Introduction to Research Design
15.521: Management Accounting and
12.810: Dynamics of the Atmosphere
15.149: Special Studies in Health
1.141J: Strategic Analysis for
9.15: Biochemistry and Pharmacology of
18.785: Analytic Number Theory
7.87: X-Ray Crystallography of Proteins and
13.018: Design of Ocean Systems Il
1.205: Advanced Demand Modeling
2.739J: Product Design and Development
6.661: Receivers, Antennas, and Signals
15.361: The Human Side of Technology
3.91J: Mechanical Behavior of Plastics
15.657J: Sustainability, Trade, and the
2.093: Computer Methods in Dynamics
4.699: Special Studies in the History,
15.435: Corporate Finance Il
15.141: Comparative Health Systems
22.084: Inventions and Patents
22.53: Statistical Processes and Atomistic
3.986: Introduction to Archaeology
4.199: Special Problems in Architectural
16.121: Low-Speed Aerodynamics
15.063: Management Decision Support
1.814J: Industrial Ecology
8.511: Theory of Solids!
4.301: Foundations in the Visual Arts
6.101: Introductory Analog Electronics
15.239: Business Organization and
1.34: Waste Containment and Remediation
11.449: Perspectives on Labor Markets
6.501: Sound, Speech, Hearing
10.546J: Principles and Methodologies of
18.100: Analysis |
2.954J: Ethical Problems in Advanced
6.734J: Application of Group Theory to the
12.453: Crosby Lectures in Geology
13.16J: Fracture of Structural Materials
2.82: Introduction to Manufacturing System
12.159: Sedimentary and Surficial Geology
15.057: Systems Optimization
18.535: Graduate Logic Seminar
10.85: (10.87) School of Chemical
15.021J: Real Estate Economics
4.235: Urbanization and Design in
12.ThU: Undergraduate Thesis
6.163: Strobe Project Laboratory
14.141: Disequilibrium Foundations of
22.ThG: Graduate Thesis
4.425: Energy in Building Design
22.562J: Spatial Aspects of Nuclear
1.383: Underground Construction
1.200: Methods for Transportation Systems
12.110: Sedimentary Geology
6.372: Design and Analysis of VLSI
4.255J: Site and Urban Systems Planning
17.186: Institutional Economics: History and
4.411: Building Technology Laboratory
4.489: Preparation for Building Technology
10.561: Molecular and Phenomenological
22.812: Nuclear Energy Economics and
24.991: Indo-European Phonology
3.932: Industrial Practice
1.105: Structural Engineering Laboratory
10.550: Process Dynamics, Operations, and
24.964: Topics in Phonology
15.348: Doctoral Seminar in Research
6.337J: Numerical Methods of Applied
2.ThG: Graduate Thesis
14.471: Public Economics |
15.656J: Technology, Law, and the Working
2.782J: Design of Medical Devices and
3.97J: Mechanical Forces in Organ
6.632: Electromagnetic Wave Theory
24.921: Special Graduate Topics in
13.42: Design Principles for Ocean
22.920: A Hands-On Introduction to Nuclear
4.614: Religious Architecture and Islamic
10.610: Applied Quantum Mechanics
6.836: Embodied Intelligence
17.ThU: Undergraduate Political Science
4.ThG: Graduate Thesis
3.60: Symmetry, Structure, and Tensor
1.155: Engineering Risk-Benefit Analysis
24.900J: The Study of Language
7.29J: Cellular Neurobiology
4.361: Dimensions of the Body
6.555J: Biomedical Signal and Image
15.369: Corporate Strategies for
1.44: Law and the Construction Industry
14.URG: Undergraduate Research
5.61: Physical Chemistry
12.602: Asteroids and Small Bodies
7.88J: The Protein Folding Problem
11.900: Doctoral Proseminars
3.641: Special Problems in Ceramics
6.115: Microcomputer Project Laboratory
11.237: Gender, Work, and Public Policy
16.55: lonized Gases
3.541: Oxidation and Corrosion of Materials
12.005: Applications of Continuum
6.823: Computer System Architecture
18.276: Mathematical Methods in
8.02X: Physics I
15.415: Finance Theory
12.710: Marine Geology and Geophysics |
2.305: Advanced Mechanical Behavior of
18.177: Stochastic Processes
6.566J: Biosensors, Signal Processing, and
15.378J: Dynamic Strategic Planning
4.441: Introduction to Building Structural
1.285J: Regional Socioeconomic Impact
4.617: Issues in Islamic Urbanism
4.266J: User Needs Programming
11.982: Graduate Tutorial
1.63: Topics in Environmental Fluid
22.581: Radiation Health Physics
10.100: Interdisciplinary Research in
22.925: Neutron and X-Ray Reflectometry
9.631: Laboratory in Cognitive Science
24.922: Special Graduate Topics in
8.334: Statistical Mechanics II
7.92J: Neurology, Neuropsychology, and
4.626: Architecture and Post-Colonial
5.932: Seminar in Physical Chemistry
16.210: Structural Mechanics II
3.981: Materials in Human Experience
1.204: Computer Algorithms in
15.433: Investments
13.26J: Design of Thermal Power
6.151: Semiconductor Devices Project
24.04J: Justice
6.334: Power Electronics
8.562: Correlations and Critical Behavior
11.427: Public Policy and Human
1.83: Environmental Organic Chemistry
16.222: Mechanics of Filamentary
13.861: Ocean and Seabed Acoustics |
17.903: Community Service: Experience and
1.231J: Planning and Design of Airport
17.254: American Political Economy
17.428: American Foreign Policy: Theory
11.430J: Managing the Real Estate
15.224: Governments, Markets, and
9.91: Topics in Cognitive Sciences
6.871: Knowledge-Based Applications
11.207: Introduction to Computers in Public
16.600: Computational Tools for Engineering
21.ThU: on page 487.
13.862: Ocean and Seabed Acoustics I
18.409: Topics in Theoretical Computer
4.601: Introduction to Art History
1.980J: Thesis Proposal Seminar
8.575J: Statistical Thermodynamics of
13.21: Ship Power and Propulsion
10.URG: Undergraduate Research
16.72: Air Traffic Control
12.560: is letter-graded.
15.070: Advanced Stochastic Processes
5.89: Special Problems in Chemistry for
4.691: Special Studies in the History,
15.575: Research Seminar in Information
3.51: Materials and the Environment
15.665: Power and Negotiation
13.990J: Oceanographic Systems |
11.256: Comparative Studies of Negotiation
72.804: Large-s
16.781J: Planning and Design of Airport
8.122: Advanced Project Laboratory
18.706: Noncommutative Algebra
3.983: The Aztec, the Maya, and Their
18.775: Algebraic Number Theory
24.942: Topics in the Grammar of a Less
7.37J: Molecular and Engineering Aspects
1.203J: Logistical and Transportation
17.168: Political Economy of
18.901: is required, but may be taken concur-
2.45J: Fundamentals of Energy in Buildings
7.61: Membranes, Receptors, and Signalling
24.962: Advanced Phonology
4.281: Transportation Economics
6.552J: Signal Processing by the Auditory
17.170: The International Politics of
15.061: Intermediate Statistics
16.871: Aerospace Product Design Tools
6.002: Circuits and Electronics
10.652: Principles and Applications of
13.64: Projects in Ocean Systems
2.060J: Principles of Acoustics
6.231: Dynamic Programming and
11.251: The Policy-Making Process
16.653: Management in Engineering
10.420: Molecular Aspects of Chemical
11.102J: Theories of Economic Development
18.115: Functions of a Complex Variable
1.202: Demand Modeling
12.800: Fluid Dynamics of the Atmosphere
17.601J: Soviet Politics and Society,
16.020: Unified Engineering I
17.UR: Undergrad
13.471J: Design and Implementation of
18.311: Principles of Applied Mathematics
10.445: Separation Processes for
1.351: Theoretical Soil Mechanics
13.04: Hydrofoils and Propellers
1.471: Management of Large-Scale Systems
11.441: Issues in Community Development
4.205: Foundations of Design and
4.613: Civic and Residential Islamic
2.744: Product Design
22.211: Nuclear Reactor Physics |
10.961: Seminar in Advanced Air Pollution
9.358: Image Representations for Vision
22.601: Fusion Energy |
13.06: Numerical Methods in Marine
6.100: is used to satisfy Departmental
3.11: Mechanics of Materials
24.210: Problems in the Philosophy of Love
22.78: Nuclear Techniques in Environmental
4.362: Dimensions of Time
22.ThU: Undergraduate Thesis
22.821: Engineering Systems Analysis
15.764: The Theory of Operations
7.546J: Principles and Methodologies of
10.975: Seminar in Polymer Science and
6.033: Computer System Engineering
6.634: Nonlinear Optics
9.021: Dynamic Neural Processing in the
4.366: Advanced Projects in Visual Arts
24.09J: Classics in Political Philosophy
5.64: Biophysical Chemistry
15.426J: Real Estate Finance and
18.756: Analysis on Lie Groups
17.522: Comparative Politics of Race and
13.013J: Systems Modeling and Dynamics II,
3.13: Structure of Materials
6.929: Undergraduate Project Presentation
17.806J: Theory of Collective Choice:
18.135: Geometric Analysis
12.507: Environmental Geophysics
15.561: Information Systems: From
4.401: Introduction to Building Technology
18.316: Seminar in Combinatorics
17.808J: Theory of Collective Choice:
18.354: Fluid Mechanics
3.52J: Materials Processing
9.75J: Psychology of Gender
17.915: Junior Colloquium in Political
10.44J: Statistical Thermodynamics of
1.573J: Introduction to Structural Mechanics
14.461: Advanced Macroeconomics |
16.423: Aerospace Physiology and Life
15.306: Behavioral Science Research
6.152J: Microelectronics Processing
11.104: Infrastructure in Developing
10.983: Reactive Processing of Materials
10.549: Tissue Engineering
13.621: Engineering Risk-Benefit
6.121J: Bioelectronics Project Laboratory
5.942: Seminar in Inorganic Chemistry
12.522: Geological Fluid Mechanics
8.311: Electromagnetic Theory
2.46J: Analysis and Design of Heating,
4.256J: Housing and Urban Policy
12.465: Structure of Geologic Aquifers
4.639: Advanced Study in 16th-, 17th-, and
4.653: Advanced Study in 20th-Century
15.672J: Labor Economics Il
1.982: Research in Civil and Environmental
1.331: Soil Dynamics
2.830: Control of Manufacturing
11.380J: Urban Transportation Planning
16.840: Real-Time Systems for Aerospace
6.561J: Fields, Forces, and Flows:
11.420J: Housing and Urban Policy
15.939: Strategic Options and Information
12.305: Global Atmospheric Pollution
12.801: Steady Circulation of the Oceans
2.851J: System Optimization and Analysis
16.984: Seminar
12.714: Computational Data Analysis
18.905: Algebraic Topology
10.910: Independent Research Problem
17.902: Political Science Internship and
15.301: Managerial Psychology Laboratory
12.990: is letter-graded.
15.035: Pricing Strategy
16.030: and 16.040 require simultaneous
16.160: Computational Fluid Dynamics
7.17: Experimental Molecular Biology:
18.425J: Cryptography and
17.530J: Politics and Enterprise in Europe
11.018: Solving the Infrastructure Crisis
15.769: Manufacturing Policy
18.725: Algebraic Geometry
17.156J: Political Economy I: Theories of
2.763: Hyperthermia: Biology, Technology,
4.488: Preparation for S.M.B.T. Thesis
5.914: Seminar in Organic Chemistry
13.61: Project Management
11.330J: Theory of City Form
15.438: Investment Banking and Markets
9.50: Research in Brain and Cognitive
17.846: Multivariate Political Analysis
2.791J: Quantitative Physiology:
18.325: Topics in Applied Mathematics
15.662: Industrial Relations and Human
1.441: Public Infrastructure Development
4.265: Behavior in the Built Environment
4.694: Special Studies in the History,
4.642: Advanced Study in Modern Art
2.061: Random Vibration
7.93: Selected Topics in Biology
15.450: Analytics of Financial Engineering
1.77: Water Quality Control
5.810: Laboratory Chemistry
15.347: Doctoral Seminar in Research
6.441: Transmission of Information
4.207: Advanced Topics in Design and
15.222: Managing International Enterprises
6.763: Applied Superconductivity
7.63: Immunology
4.426: Energy, Environment, and Buildings
18.034: Differential Equations
22.091: Special Topics in Nuclear
11.484: Project Evaluation and Planning in
9.03: Neural Basis of Learning and Memory
3.595: Special Problems in Materials
7.15: Experimental Molecular Biology:
10.571J: Air Pollution Control
2.95J: Real-World Ethics
3.471: Advanced Topics on the Physics and
22.64: Plasma Kinetic Theory
14.24: Law and Economics
14.691J: Research Seminar in Industrial
9.371: Advanced Seminar on Inference and
8.235: Superconductivity
1.472: Innovative Contract Strategies in the
11.305: Landscape Ecology and Urban
10.668J: Statistical Mechanics of Polymers
1.81J: Chemicals in the Environment:
2.157J: Design and Implementation of
15.565: Information Technology Il:
11.122: Environmental Policy and Regulation
1.431: Structuring Construction Industry
11.962: Urban Fieldwork and Internships
5.511: Synthetic Organic Chemistry |
8.614J: Introduction to Plasma
12.816: Numerical Modeling of the
15.601: The American Legal System
12.721: Special Problems in Marine Geology
2.793J: Quantitative Physiology: Sensory
6.872: Medical Computing
7.98J: Neural Plasticity in Learning and
1.594J: Composite Materials
11.303J: Design for Urban Development
24.961: Introduction to Phonology
12.550: Geosystems |
17.603: Soviet and Post-Soviet Politics and
12.650: Current Topics in Planetary
4.405: Materials and Construction
15.834: Marketing Strategy
1.732: Hydrologic Estimation and Prediction
16.67: Engineering Internship
18.705: Commutative Algebra
10.95: Special Problems in Chemical
15.084J: Nonlinear Programming
1.366: Geotechnical Engineering
12.340J: Atmospheric Chemistry
16.14: Transition and Turbulence
4.624: Architecture and Modernization in the
10.972: Biochemical Engineering Research
2.31: Finite Element Analysis in Computer
15.564: Information Technology I
12.823: Ocean Modeling
6.930: Management in Engineering
18.915: Graduate Topology Seminar
7.13: Experimental Microbial Genetics
6.847: Dataflow Architecture and
5.512: Synthetic Organic Chemistry Il
6.521J: Quantitative Physiology: Cells and
6.901: Inventions and Patents
16.83: Space Systems Engineering
9.591: Language Processing
14.21J: Health Economics
16.295: Failure Mechanics of Composite
8.12: Physics Project Laboratory
17.560J: Technology, Policy, and
15.379: Seminar in Management of
10.581J: Materials Processing
18.014: Calculus with Theory
6.038: Artificial Intelligence in Practice
15.811: Marketing Management
17.532: Japan and the New World Order
1.27: Studies in Transportation
6.456J: Sonar, Radar and Seismic Signal
12.822: Nonlinear Wa’
18.703: together form a standard algebra se-
16.872: Aerospace Design Project
211.422: Tragedy
10.421: Heterogeneous Catalysis and
10.979: Plasma Processing
1.80: Fundamentals of Ecology
7.20: Human Physiology
6.792: Special Topics in the Solid State and
3.49: Special Problems in Electronic
8.333: Statistical Mechanics |
14.462: Advanced Macroeconomics I
1.201: Transportation Systems
17.410: Political Economy of Global Change
2.55: Advanced Heat and Mass Transfer
11.369: Science and Technology in
15.315: Planning and Managing Change
17.805: Theory of Collective Choice:
2.952: Advanced Engineering Internship
7.22: Developmental Biology
9.201: Advanced Animal Behavior
15.770J: Transportation and Logistics
12.456: Seminar in Rock Mechanics
6.161: Modern Optics Project Laboratory
3.987: Human Origins and Evolution
15.635: Law and International Business
15.075: Applied Statistics
18.737: Quantum Groups
15.783J: Product Design and Development
4.645: Selected Topics in Architecture —
8.642: Physics of High-Energy
5.071: Biochemistry by sri 12: 5.07, 5.310°
4.662: Advanced Study in the History of
2.953J: Research Ethics
15.824: Advertising, Promotion, and
8.902: Astrophysics II
17.816: Field Research Methods in
13.10J: Introduction to Structural Mechanics
12.808: Introduction to Observational
2.067J: Structural Acoustics
1.381: Rock Mechanics
6.961: Introduction to Research in Electrical
1.64: Dynamics of Stratified Fluids
3.31: Phase Transformations
1.51: Design of Steel Structures
6.652J: Introduction to Plasma
8.624: Plasma Waves
22.38: Probability and its Applications To
1.71J: Introduction to Hydrology
2.670: Mechanical Engineering Tools
16.221: Structural Dynamics
17.253: American Political Economy
18.433: Combinatorial Optimization and
22.031: Engineering of Nuclear Reactors
2.822: Design and Manufacture with
17.482J: US General Purpose Forces
2.152: Nonlinear Control System Design
11.339: Downtown
8.323: Relativistic Quantum Field
4.461: Building Simulation
5.48J: The Protein Folding Problem
1.61: Environmental Fluid Transport
5.891: Special Topics in Chemistry for
6.035: Computer Language Engineering
24.973: Advanced Semantics
14.671J: Labor Economics |
12.330J: Fluid Physics
17.602: Soviet and Post-Soviet Politics and
1.39: Studies in Geotechnical
24.965: Morphology
1.571: Structural Analysis and Control
13.022: Marine Hydrodynamics I
18.419: Seminar in Theoretical Computer
8.289: Techniques of Radio Astronomy
15.074: Mathematical Models and Policy
12.515: Data Analysis: Model Parameter
1.60: Environmental Fluid Transport
1.725J: Chemicals in the Environment: Fate
15.779: Manufacturing Management
2.05: Kinematics and Dynamics of
12.865: Ocean Data and Ocean Models I!
17.614J: Russian Science, Technology, and
12.620J: Variational Mechanics: A
17.901: Political Science Internship and
215.760: and 15.762 are half-term subjects.
48.701: lgebra|, 12
16.523: Environmental Aerospace
1.811J: Environmental Law: Pollution
2.004J: Systems Modeling and Dynamics Il
3.94: Morphology of Polymers
16.050: Thermal Energy
10.570J: Chemicals in the Environment:
24.233J: Political Philosophy
15.370: Strategic Management for
24.959: Workshop in Syntax and
6.781: Submicrometer and Nanometer
12.716: Igneous Processes at Oceanic
22.012: Seminar in Fusion and Plasma
12.512: High-Frequency Seismology
18.795: Multilinear Algebra
6.242: Advanced Linear Control
22.612J: Introduction to Plasma
15.078: Quality Improvement Via Statistics
18.458: Robust Statistics and
4.641: 19th-Century Art
11.225: Modes of Argumentation and
2.812: The Design and Control of
6.848J: Theory of Parallel and VLSI
11.022J: American Living Standards and
1.286: Freight Transportation
12.862: Dynamics of Shelf Circulation |
9.URG: Undergraduate Research
8.312: Electromagnetic Theory
6.455J: Sonar, Radar and Seismic Signal
10.390: Process Design
10.976: Process Design, Operations, and
3.930: Industrial Practice
4.273: Introduction to Design Inquiry
11.462: Housing Problems and Policies in
18.308: Wave Motion
8.901: Astrophysics |
6.080J: Practicum in Engineering Writing
3.53: Electrochemical Processing of
16.ThG: Graduate Thesis
4.203: Geometric Modeling
10.990: Introduction to Chemical
16.851: Satellite Engineering
13.851: Fundamentals and Applications of
14.451: Macroeconomic Theory |
12.313: Climate Change: Past, Present, and
15.810: Introduction to Marketing
15.342J: Organizations and Environments
12.410J: Observational Techniques of
9.369: Computational Neuroscience
15.019: International Trade and
12.742: Marine Chemistry
16.300: Measurement, Estimation, and
12.475: Global Plate Tectonics
6.805J: Ethics and the Law on the Electronic
3.56: Engineering Systems Analysis
8.896J: Supersymmetric Quantum Field
17.422: Contending Paradigms of
17.205: Health Policy
1.969: Graduate Studies in Civil and
4.663: History of Urban Form
11.254: Public Sector Economics for
15.UR: Undergraduate Research in
8.361: Quantum Theory of Many-Particle
3.ThG: Graduate Thesis
18.575: Model Theory
4.451: Building Systems
4.647: Advanced Study in the Theory and
1.25J: Technology, Policy, and
6.335: Fundamental Theory of Nonlinear
12.803: Quasi-balanced Circulations in
5.931: Seminar in Physical Chemistry
1.40: Project Management
18.386: Advanced Nonlinear Dynamics and
12.540: Principles of Global Positioning
16.651: Computer Models of Physical and
15.341: Individuals, Groups, and
24.957: Introduction to Linguistic Theory at
1.591J: Fracture of Structural Materials
12.863: Dynamics of Shelf Circulation Il
7.81: Frontiers in Modern Plant Biology
14.25J: Aerospace Economics
17.109J: Philosophy of Law
8.322: Quantum Theory Il
15.343: Managing Transformations in Work,
6.854J: Advanced Algorithms
18.UR: Undergraduate Research
15.876: Principles of Dynamic Systems
12.333: Atmospheric and Ocean Circulation
15.215: International Dimensions of
1.461: Corporate Organization For the Future
18.906: Algebraic Topology
11.362: Environmental Management
17.252: Congress and the American
1.URG: Research in Civil and Environmental
11.365J: Environmental Management of the
11.480: Theory and Practice of Privatization
15.136J: Health Technology
14.389: Econometrics Paper
16.333: Advanced Flight Dynamics and
16.335: Spacecraft Dynamics and Control
24.119: Minds and Machines
22.33: Nuclear Engineering Design
7.99: Disease Intervention Through
13.94: Law for Ocean Systems
1.233J: Seminar in Air Transportation
16.683: Aeronautics and Astronautics
11.335J: Cities of Tomorrow
15.451: Proseminar in Financial Engineering
15.936: Applied Corporate Analysis
18.314: Combinatorial Analysis
6.341: Discrete-Time Signal Processing
18.08: Differential Equations
42.311: Experimental he dts
4.665: Contemporary Architecture and
22.69: Plasma Laboratory
1.251J: Transportation and Government —
5.62: Physical Chemistry
6.826: Principles of Computer Systems
12.743: Geochemistry of Marine
17.207: Race and Science
18.423J: Computability, Logic, and
12.707: Pre-Pleistocene Paleoceanography
15.452: Proseminar in Financial Management
24.992: Survey of General Linguistics
9.05: Neural Basis of Movement
11.304J: Site and Urban Systems Planning
18.747: Infinite-dimensional Lie Algebras
22.76: Nuclear Chemical Engineering
16.621: Experimental Projects |
22.92: Advanced Engineering Internship
10.441J: Molecular and Engineering
1.723: Groundwater Quality and Remediation
1.256J: Technology, Policy, and
15.511: or 15.515 or 15.516
1.284J: Regional Economic Theories,
16.682: Selected Topics in Aeronautics and
1.04: Solid Mechanics (3-2-7)
4.442: Introduction to Building Structural
3.08J: Industrial Competition in the US and
6.041: Probabilistic Systems Analysis
15.539: Doctoral Seminar in Accounting
18.315: Combinatorial Theory
22.63: Engineering Principles for Fusion
5.UR: Undergraduate Research
3.291: Special Problems in Materials
22.021: Nuclear Reactor Physics
17.184J: Economic Institutions and Growth
9.110J: Neurology, Neuropsychology, and
15.655J: Law, Technology, and Public
15.692J: Research Seminar in Industrial
13.09: Potential Flows
13.83J: Structural Acoustics
18.443: Statistics for Applications
11.481J: Regional Economic Theories,
1.999: Undergraduate Studies in Civil and
1.322: Soil Behavior
6.980: Teaching Electrical Engineering
1.66: Problems in Water Resources and
6.432: Stochastic Processes, Detection, and
15.691J: Research Seminar in Industrial
15.516: Introduction to Financial and
12.114: Field Geology |
16.521: Aircraft Turbine Engine Design
1.45: Construction Finance
6.022J: Quantitative Physiology: Organ
6.291: Seminar in F
15.441J: Advanced Financial
18.465: Topics in Statistics
11.466: Common Property Resources
9.88: Origins of Behavior
14.40: Advanced Macroeconomics
22.561J: Magnetic Resonance — Analytic,
2.303: Micro Mechanisms of Fracture
16.28: Adaptive Materials and Structures
16.322: Stochastic Estimation and Control
15.698: Special Seminar in Industrial
3.941J: Statistical Mechanics of Polymers
12.519J: Sonar, Radar and Seismic Signal
22.823: Nuclear Industry Dynamics
17.424: International Political Economy of
4.171: The Space Between Workshop
2.010: Control System Principles
12.841: Climate Modeling
18.769: Topics in Lie Theory
22.57J: Radiation Biophysics
4.616: Cultural Signification in Architecture
3.985J: Archaeological Science
12.484: Directed Field Studies
6.111: Introductory Digital Systems
10.11: Computer Models of Physical and
15.599: Workshop in Information Technology
11.437: Financing Community Economic
16.82: Flight Vehicle Engineering
6.036: Problem-Solving Paradigms
15.545: Mergers and Acquisitions: The
1.37: Geotechnical Measurements and
6.921: VI-A Internship
15.766: Total Quality Management
11.223: Introduction to Modes of
15.578: Communications and Connectivity
22.77: Nuclear Waste Management
17.460: Defense Politics
3.50: High-Temperature Physical Chemistry
13.ThG: Graduate Thesis
6.343: Digital Speech Processing
14.772: Development Economics:
6.835: Concurrent Systems for Artificial
11.015J: Riots, Strikes, and Conspiracies in
24.221: Metaphysics
15.432: Capital Markets and Financial
24.205: The Good Life
7.16: Experimental Molecular Biology:
18.965: Geometry of Manifolds 18.ThG Graduate Thesis
12.451: Seminar in Regional Tectonics
15.439: International Corporate Finance
17.550J: Property Rights Under Transition
3.29: Special Problems in Materials
12.611: Advanced Planetary Observations
1.589: Studies in Structural Design and
18.358: Hydrodynamic Stability and
12.831: Dynamics of the Middle
8.399: Physics Teaching
16.800J: Aerospace Economics
15.812: Marketing Management
11.302J: Urban Design Politics
15.240: Business Organization and
1.541: Behavior of Concrete Structures
10.02J: Biotechnology and Engineering
11.332J: Urban Design
12.741: Marine Geochemistry
15.081J: Introduction to Mathematical
16.323: Principles of Optimal Control
18.700: Linear Algebra
2.943: Engineering Risk-Benefit Analysis
12.601: Essentials of Planetary Science
13.82J: Sound and Structural Vibration
16.652: Inventions and Patents
24.701: Topics in Logic
22.070J: Materials for Nuclear Applications’
18.511: Introduction to Mathematical Logic
18.415J: Advanced Algorithms
18.318: Topics in Combinatorics
9.02: Brain and Behavior Laboratory
6.840J: Theory of Computation
10.978: Seminar in Applied
18.727: Topics in Algebraic Geometry
16.985J: Proseminar in Manufacturing
5.60: Thermodynamics and Kinetics
22.615: MHD Theory of Fusion Systems
3.701: Special Problems in Metallurgy
22.912: Seminar in Nuclear Engineering
2.93J: Engineers, Scientists, and Public -
15.820: Advanced Marketing
22.56J: Principles of Medical Imaging
17.844: Categories and Concepts in Political
12.711: Marine Geology and Geophysics Il
9.363: Research in Natural Computation
1.59: Mechanics of Construction Materials
1.364: Advanced Geotechnical Engineering
11.464: The Informal Sector and the
17.801: Political Science Laboratory
4.242J: Advanced Seminar in City Form
16.150: Unsteady Fluid Mechanics
24.966J: Laboratory on the Physiology,
2.982: Microscale Heat Transfer
2.75: Precision Machine Design
5.52: Advanced Biological Chemistry
6.633: Electrodynamics of Waves, Media,
15.314: Power and Culture in Organizations
13.413: Projects in Naval Ships Conversion
12.551: Geosystems Il
14.453: Macroeconomic Theory Ill
8.ThG: Graduate Physics Thesis
11.306: Impact Assessment Techniques
16.458J: Biomedical Instrumentation
22.926: Environmental Applications of
15.329: Special Seminar in Organization
3.92J: Composite Materials
15.535: Business Analysis Using Financial
1.254J: Infrastructure in Developing
1.782: Environmental and
6.637: Optical Information Processing
6.931: Development of Inventions and
1.255J: Political Economy and Technology
14.64: Labor Economics and Public Policy
12.481: Advanced Field Geology |
24.901J: Language and its Structure I:
18.781: Theory of Numbers
6.801: Machine Vision
12.840: Past and Present Climate
17.524: Nationalism
12.518J: Sonar, Radar and Seismic Signal
12.812: General Circulation of the Earth’s
2.721: Design for Production
17.209: Race and the American Legal
17.110: New Currents in Social Theory
16.77: Flight Transportation Operations
13.017: Design of Ocean Systems |
11.525: New and Developing Technologies
14.441J: Advanced Financial
12.120: Environmental Earth Science Field
3.00: Thermodynamics of Materials
17.573: Political Dimensions of African
10.989: Special Topics in Biotechnology
3.54J: Corrosion: The Environmental
10.792J: Proseminar in Manufacturing
6.071: Introduction to Electronics
17.468: Foundations of Security Studies
22.70J: Materials for Nuclear
1.542: Behavior of Steel Structures
22.86: Entrepreneurship
12.109: Petrology
13.81J: Principles of Acoustics
1.ThG: Graduate Thesis
2.810: Fundamentals of Manufacturing
5.72: Statistical Mechanics
6.430J: Engineering Probability and
10.90: Independent Research Problem
6.182: Psychoacoustics Project Laboratory
8.01X: Physics |
15.935: Corporate Strategies and Practices
15.ThG: Graduate Thesis
8.811: Particle Physics II
1.148J: Economics of Project Evaluation
17.328J: Science and Technology in
18.175: Theory of Probability
11.255: Bargaining, Negotiation, and Dispute
6.371: Introduction to VLSI Systems
10.33: Analytical Treatment of Chemical
12.476: Radiogenic Isotope Geology
2.852: Manufacturing Systems Analysis _
22.616: Plasma Transport Theory
4.280: Architecture Internship
4.222: Aspects of Office Practice
24.993: Tutorial in Linguistics and Related
16.66: Industrial Practice
1.129: Information Content of the
8.641: Physics of High-Energy
18.585: Set Theory
3.566: Entrepreneurship
24.151: Introduction to Philosophy of
5.53: Molecular Structure and Reactivity
17.483J: US General Purpose Forces
14.29: Topics in Political Economy
16.431: Flight Simulation and Virtual
10.520: Molecular Aspects of Chemical
4.351: Introduction to Video
8.711: Nuclear Physics
16.73J: Seminar in Air Transportation
3.984: Materials in Ancient Societies: Metals
2.273: Turbulent Flow and Transport
11.258J: Organizations and Environments
2.062: Wave Propagation
12.950: is letter-graded.
2.156J: Dynamics of Nonlinear Systems
3.ThU: Undergraduate Thesis
10.470J: Environment and Technology
15.414: Financial Management
13.472J: Computational Geometry
10.548J: Transport Phenomena and Tumor
2.29J: Air Pollution Control
4.172: Form Language Workshop
11.442: Strategies in Community
12.455: Megascopic Strain Analysis in
4.388: Preparation for S.M.Vis.S. Thesis
10.962: Seminar in Molecular Cell
11.465J: Special Interest Group in Urban
17.547: Chinese Politics and Political
15.352: Management of Technological
15.574: Theoretical Foundations for
1.12: Computer Models of Physical and
1.714: Surface Hydrology
10.332: Linear Operator Theory in Chemical
2.79J: Biomaterials — Tissue Interactions
9.520: Learning, Approximation, and
2.003: or 3.185 or 6.001 or 10.301 or
1.252J: Urban Transportation Planning
6.751: Quantum Electronics
3.711J: Materials for Nuclear
9.ThG: Graduate Thesis
12.563: Seminar in Earthquake Source
6.263: Data-Communication Networks
17.558J: Political Economy and Technology
4.241J: Theory of City Form
11.196: Urban Fieldwork and Internships
11.208: Introduction to Computers in Public
10.001: Introduction to Computer Methods
9.651: Cognitive Processes
22.58: Seminar in Radiation Health Physics
24.809J: Objectivity, Truth, and Scientific
15.576: Research Seminar in Information
12.467: Seminar in Geomorphology
15.825: Marketing Decision Support
18.904: Seminar in Topology
6.251J: Introduction to Mathematical
1.91: provides credit for the first two work as-
12.802: Wave Motions in the Ocean and
24.231: Ethics
22.351: Current Nuclear Fuel Cycle Issues
11.447: Housing Finance
2.820: The Design and Control of Manufacturing Systems, 12; 2.810° (6A, 3D, 3L)
17.ThG: Graduate Political Science
4.341: Introduction to Photography
18.445: Introduction to Stochastic
4.106: Design Skills Workshop
15.436: International Financial Markets
22.59: Principles of Nuclear Radiation
11.257: Research Seminar on Theory-
4.126: intended for juniors and seniors.
13.462: Projects in Ocean Engineering
6.331: Advanced Circuit Techniques
13.013: Systems Modeling and Dynamics II
13.010: Introduction to Ocean Science and
4.660: The Architectural Agenda
9.63: Laboratory in Cognitive Science
18.504: Seminar in Logic
11.432J: Real Estate Capital Markets
2.648: Superconducting Magnets
10.94: Special Problems in Chemical
15.829: International Marketing
15.066J: System Optimization and Analysis
10.982: Special Topics in Experimental
10.986: Gas-Solid Reactions
17.501: Introduction to Comparative
9.011J: Principles of Neuroscience
12.804: Large-scale Flow Dynamics
16.010: and 16.020 require simultaneous
15.671J: Labor Economics |
15.941J: Managing the Real Estate
17.559J: Technology, Policy, and
13.15: Materials for Ocean Engineering
22.103: Microscopic Theory of Transport
14.778J: Economic Institutions and Growth
16.75: Airline Management
6.199: Advanced Undergraduate Project
5.74: Introductory Quantum Mechanics Il
17.543: Political Change in Latin America
15.412: Financial Management Il
12.805: Laboratory in Physical
14.296J: Theory of Collective Choice:
3.980: Ancient Mexican Bells: Technology
24.808: Rationality and Action
16.URG: Undergraduate Research
14.71: Historical Perspectives on Current
24.235J: Philosophy of Law
12.740: Quaternary Paleoceanography
2.615: Internal Combustion Engines
6.720: Integrated Microelectronic Devices
8.515J: Biological Physics
11.487: Public Finance in Developing
13.465: Ocean Instrument Field Laboratory
2.921J: Deformation and Fracture of
6.838J: Advanced Topics in Computer
1.32: Introduction to Engineering Geology
17.430: Research Seminar in International
11.205: Planning and Institutional
15.826: Channels of Distribution
2.796J: Quantitative Physiology: Organ
12.520: Geodynamics
13.801: Mechanical Vibration
16.76J: Logistical and Transportation
5.32: Intermediate Chemical Experimentation
4.210: Light, Color, and Computer Graphics
7.97: Topics in Evolution
13.991J: Oceanographic Systems Il
14.75J: Theories of Economic Development
12.300: Global Change Science
15.URG: Undergraduate Studies in
5.URG: Undergraduate Research
22.811: Energy, Electricity, and the
18.441: Statistical Inference
1.691: Surface Wave Dynamics
9.33: Methods in Neural Modeling
12.312: Climate System Computer Lab
2.306: Dislocations and Mechanical
8.921: Stellar Structure and Evolution
18.356: Rotating Fluids
15.660: Industrial Relations and Human
15.677J: Public Policy and Human
15.937: Proseminar in Strategic
17.462: Innovation in Military Organizations
1.597: Studies in Construction Materials
10.491: Integrated Chemical Engineering II
22.45: Lattice Gas Algorithms and
5.76: Molecular Spectra and Molecular
1.713: — Introduction to Hydrology, 12; 1.03, 1.05" 1.813 Chemicals in the Environment: Toxicology, 12;
16.681: Special Projects
5.33: Advanced Chemical Experimentation
17.106J: Political Philosophy
15.434: Corporate Finance!
15.961: Special Studies in Management
5.002: Mechanics and Materials li, 12; 2.001
16.241: Advanced Structural Dynamics
14.76: Income Distribution
1.10J: Environment and Technology
2.159J: Computer Aided Engineering |
6.243: Dynamics of Nonlinear Systems
16.312: Feedback Control Systems, 12; ar 060
22.314J: Structural Mechanics in Nuclear
6.ThG: Graduate Thesis
18.917: Topics in Algebraic Topology
15.512: Managerial and Financial Accounting
16.456J: Biomedical Signal and Image
1.127J: Design and Implementation of
6.313: Contemporary Computer Design
12.718: Kinetics and Mass Transport
17.319: Environmental Politics and Policy
11.020: Poverty, Public Policy, and
1.38: Engineering Geology
2.54: Heat Transfer
14.65J: American Living Standards and
12.130: Structure of Geologic Aquifers
18.446: Applied Time-Series Analysis
6.946J: Variational Mechanics: A
9.65: Cognitive Processes
4.188: Preparation for M.Arch. Thesis
4.455: Integrated Building Systems
3.80J: Proseminar in Manufacturing
1.432J: Project Control
2.06J: Mechanical Vibration
18.701: Algebra |
22.078: Nuclear Techniques in
4.481: Building Technology Seminar
17.260: Graduate Seminar in American
4.695: Special Studies in the History,
11.491J: Industrial Development and Policy
2.800: Tribology
2.74: Optimal Product Redesign
6.868J: The Society of Mind
6.685: Electric Machines
18.338J: Introduction to Numerical
17.544: Comparative Politics of Latin
17.115J: Justice
12.479: Trace-Element Geochemistry
3.43: Electronic Materials and Devices
3.596: Special Problems in Materials
12.311: Experimental Oceanography
17.516: Retribution and Reparations
8.712: Advanced Topics in Nuclear
22.602: Fusion Energy Il
9.671J: Problems of Mental
8.942: Cosmology
16.64: Flight Measurement Laboratory
10.920: Indepartmenta!l Seminar in
15.079: Applied Multivariate Methods
4.163J: Urban Design
6.601: Fields, Forces, and Motion
17.172J: Technology, Productivity, and
1.82: Problems in Aquatic Biology and
16.060: Principles of Automatic Control, 12; 16.030-16.040
24.948J: Linguistic Theory and Second
6.866: Machine Vision
18.426J: Advanced Topics in
9.62: Introduction to Cognitive Science
2.601J: Design of Thermal Power
6.853: Computer Systems
3.982: The Ancient Andean World
13.411: Methods of Naval Ship-System
2.999: Engineer's Degree Thesis Proposal
4.325: Advanced Sculpture
7.47: Biological Oceanography
15.879: Research Seminar in System
6.001: Structure and Interpretation of
2.737: Mechatronics
17.113J: Classics in Political Philosophy
14.128: Dynamic Optimization and
18.565: Recursion Theory
15.645: Government and the Management of
4.276: Design Research Seminar
18.979: Graduate Geometry Seminar
17.101: What is Politics?
7.75J: Topics in Metabolic Biochemistry
4.252J: Urban Design and Development
14.28: Competition in Telecommunications
9.59J: Psycholinguistics
9.20: Animal Behavior
15.316: Organizational Leadership and
4.288: Preparation for S.M.Arch.S. Thesis
1.85: Wastewater Treatment Engineering
13.414: Projects in New Construction Naval
4.471: Control of Space Conditioning
4.602: Modern Art and Mass Culture
4.635: Renaissance Architecture
15.666: Negotiation and Conflict
17.476J: Analysis of Strategic Nuclear
14.672J: Labor Economics I
18.715: Topics in Homological Algebra
10.980: Macrotransport Processes
1.151: Probability and Statistics in
14.731: Economic History
10.992: Seminar in Chemical
1.699J: Special Projects in Oceanographic
15.328: Special Seminar in Organization
4.372: Environmental Art
24.241: Logic!
8.321: Quantum Theory |
7.96: Cell-Cell Signaling
11.333J: Urban Design Seminar
2.158J: Computational Geometry
15.674J: Managing People and
17.575: Introduction to Contemporary
8.ThU: Undergraduate Physics Thesis
15.515: Financial and Managerial Accounting
16.981: Advanced Special Project
13.60: Ship Production
16.622: Experimental Projects II
6.070J: Electronics Project Laboratory
11.366: Planning for Sustainable
16.89: Space Systems Engineering
16.242: Aeroelasticity
4.494: Special Problems in Building
15.828: New Product Development
14.111J: Economics of Project
13.62: Engineering Systems Analysis
2.58J: Radiative Transfer
15.582J: Information and Communications:
16.870: Aerospace Product Design
6.938: Engineering Risk-Benefit Analysis
15.065: Decision Anal
15.353: Managing Innovation and
11.469J: Infrastructure in Developing
18.786: Topics in Number Theory
8.421: Atomic and Optical Physics |
2.165: Robotics and Mechatronics
13.470J: Computer Aided Engineering |
11.337J: Environmental Design Policy and
15.501: as prerequisites.
3.05: Computer Models of Physical and
1.ThU: Undergraduate Thesis, 1
13.43: Design of Ocean Engineering
6.522J: Quantitative Physiology: Organ
17.166: Problems of Advanced Industrial
12.814: Global Transport Modeling
17.245: The Supreme Court and
24.209J: Studies in Film and Media:
18.969: Topics in Geometry
2.794J: Quantitative Physiology: Cells and
1.124J: Computer Aided Engineering |
6.775: Design of Analog MOS LSI
6.UR: Undergraduate Research in Electrical
17.920: Special Topics in Political Science
10.582J: Plasma Processing in Integrated
10.805J: Technology, Law, and the Working
14.194: Seminar: Topics in Economics
10.471: Introduction to Air Pollution
10.816: Engineering Risk-Benefit
3.01: Physical Chemistry of Materials
14.781J: Political Economy I: Theories of
6.542J: Laboratory on the Physiology,
15.699: Special Seminar in Industrial
17.158: Political Economy of West
17.588: Field Seminar in Comparative
18.758: Representations of Lie Groups
13.998: Principles of Oceanographic
24.208: Kant
14.72: Capitalism and Its Critics
11.932: Preparation for Thesis
15.138J: Seminar on Pharmaceutical and
4.364: Dimensions in Space
16.862: Engineering Risk-Benefit
2.51: Heat and Mass Transfer Engineering
12.511: Low-Frequency Seismology
4.440: Basic Structural Theory
22.101: Applied Nuclear Physics
16.334: Advanced Control of Flight
11.363J: Chemicals in the Environment:
5.071J: Biochemistry Laboratory
2.302: Physics of Inelastic Deformation of
14.442J: Advanced Financial Economics Ill
15.058: Introduction to Management Science
17.540: Politics and Policy in Contemporary
9.891: Cognitive Development
24.113: Classical Film Theory: Problems in
12.870: Air-Sea Interaction: Boundary Layers
13.774: Advanced Engineering Internship
3.33: Defects in Crystals
15.059: Optimization Modeling for Managers
4.371: Art and the Environment
12.006: Chaos and Complexity
11.234: Making Sense: Qualitative Methods
15.978: Seminar in Management |!
13.51: Computer Models of Physical and
1.03: Introduction to Probability and
16.401J: Quantitative Physiology: Sensory
12.509: Earthquakes and Faulting
15.794: Research Project in
2.063J: Sound and Structural Vibration
6.034: Artificial Intelligence
6.281J: Logistical and Transportation
2.41J: Thermal Power Engineering
12.ThG: Graduate Thesis
2.891: Management for Engineers
1.592: Mechanical Behavior of Construction
6.875J: Cryptography and Cryptanalysis
15.611: The American Legal System
4.427J: Analysis and Design of Heating,
8.952: Particle Physics of the Early
7.65J: Principles of Neuroscience
11.41: Discourse on Social Policy
12.401: Beyond the Solar System
11.014J: American Urban History I
18.437J: Distributed Algorithms
12.331: Fluid Dynamics of the Atmosphere
2.73: Design Projects
3.092: Perspectives in Materials Science
9.931: Research Reports
13.741J: Sonar, Radar and Seismic Signal
16.123: Gases and Fluids in the Space
6.312: Acoustics
24.958: Linguistic Structure
11.210: Political Economy for Planners |
8.731: Nuclear Physics Seminar
11.221: Quantitative Reasoning and
14.674J: Managing People and
15.322: Organizational Psychology and
12.450: Seminar in Geology and
2.ThU: Independent Study or Thesis, .6*
10.21: Structures and Properties of Matter
17.420: Theories of International
3.70: Special Problems in Metallurgy
17.167: Political Economy of Asi
17.412: Evolution of International
24.946: Linguistic Theory and Japanese
9.919: Teaching Brain and Cognitive
15.760: primarily for graduate students in Sloan
1.593J: Mechanical Behavior of Plastics
2.181J: Human Factors Engineering
1.46: Strategic Management in the Design
3.577: Engineering Risk-Benefit Analysis
6.686: Advanced Power Systems |
11.235: Analyzing Projects and
6.735J: Modern Topics in Solid State
12.320J: Introduction to Hydrology
3.30: Electron Microscopy: Image
15.220: international Management
18.238: Geometry and Quantum Field
1.583: Nondestructive Evaluation of
10.74J: Radiative Transfer
5.941: Seminar in Inorganic Chemistry
16.74: Air Transportation Economics
13.80J: Mechanical Vibration
18.510: Introduction to Mathematical Logic
13.5: subjects including one laboratory. Two
15.795: Seminar in Operations
3.903J: Student Seminar in Polymer Science
15.067: Competitive Decision Making and
2.951: Engineering Internship
22.54: Nuclear and Atomic Collision
6.772: Compound Semiconductor Devices
15.931: Strategic Management
12.478: Pressure-Temperature-Time
24.952: Advanced Syntax
13.39: Analysis of Techniques for
2.781J: Biomedical Instrumentation
16.230: and Shelis
10.960J: Student Seminar in Polymer
11.340J: Legal Issues in the Development
10.984: Biomedical Applications of
1.70: Environmental Engineering Clinic
2.277: Biomedical Fluid Mechanics
3.81: Engineering Probability and
1.812J: Regulation of Chemicals, Radiation,
16.29: Advanced Topics in Filamentary
1.715: Environmental Data Analysis
15.932: Technology Strategy
6.821: Programming Languages
6.936: Entrepreneurship
22.013: Applications in Radiation Science
13.07: Free Surface Hydrodynamics
15.234J: Comparative Organization
14.581: international Economics |
14.UR: Undergraduate Research
8.282: Introduction to Astrophysics and
12.830: Topics in Waves and Instability
6.732: Physics of Solids
1.58: Constructed Facilities Project
15.437: Options and Futures Markets
15.792J: Proseminar in Manufacturing
16.58: Aircraft Gas Turbine Structures
14.31: Econometrics
10.981: Seminar in Colloid and
4.214J: Advanced Topics in Computer
4.204: Advanced Projects in Geometric
17.526: Dissertation Workshop in European
13.03: Responses of Marine Structures to
7.02: Introduction to Experimental Biology
15.615: The Manager’s Legal Function
10.ThU: Undergraduate Thesis
11.002: Introduction to Public Policy
6.333: Electronic Circuits
17.577: The Politics of Change in the Third
15.238: Busine: nization and
2.785J: Mechanical Forces in Organ
15.568: Management Information Systems
12.712: Advanced Marine Seismology
10.940J: Seminar on Pharmaceutical and
15.416J: Introduction to Financial
4.394: Special Problems in Visual Arts
15.658: Legal Issues in the Development
22.32: Nuclear Power Reactor Synthesis
12.517: Dynamics of Complex Physical
3.UR: Undergraduate Research
2.084J: Structural Mechanics in Nuclear
11.381J: Public Transportation Service and
11.482J: Regional Socioeconomic Impact
6.651J: Introduction to Plasma
9.322J: Genetic Neurobiology
15.933: Advanced Strategic Management
11.200: Planning and Institutional Processes
15.577: Software Engineering
9.641: Introduction to Neural Networks
13.UR: Undergraduate Research
7.67J: Genetic Neurobiology
10.535: Interfacial Transport Processes and
18.313: Probability
9.34J: Cognitive Architectures
1.721: Advanced Subsurface Hydrology
15.934: Internal Organization, Strategy, and
6.551J: Acoustics of Speech and Hearing
10.331: Nonlinear Analysis in Chemical
15.581: Information Systems and Law
24.905J: Psycholinguistics
11.431J: Real Estate Finance and
4.173: Small Built-Collage
20.ThG: Graduate Thesis
2.100: Information and Probability
6.431: Applied Probability
14.54: International Trade
11.433J: Real Estate Economics
17.539: Politics and Policy in Contemporary
2.761J: Principles of Medical Imaging
16.26: Thermal Structures
4.264: Environmental Psychology
14.416J: Introduction to Financial
24.970: Introduction to Semantics
4.627: Special Problems in Islamic and
5.311: Introductory Chemical
9.036: The Visual System
6.641: Microwave Circuits
5.ThG: Graduate Thesis
14.454: Macroeconomic Theory IV
3.070J: Materials for Nuclear Applications
15.249: Special Seminar in International
18.776: Algebraic Number Theory
14.294: Seminar in Political Economy
6.673: Introduction to Numerical Simulation
8.613: Introduction to Plasma Physics |
5.63: Molecular Spectroscopy: Laser and
12.452: Mechanics of Sedimentary
13.112: Safety of Marine Systems
6.344: Two-Dimensional Signal and
5.07: Biological Chemistry
1.76: Aquatic Chemistry
4.URG: Undergraduate Research in
6.03: Principles of Inorganic bee iid 12; 5.12 6.32 Intermediate ene Experimentation, 15;
22.71J: Physical Metallurgy
14.452: Macroeconomic Theory Il
4.250J: Introduction to Urban Design and
6.012: Electronic Devices and Circuits
10.84: (10.86) School of Chemical
3.96J: Biomaterials — Tissue Interactions
17.484: Comparative Grand Strategy and
22.911: Seminar in Nuclear Engineering
4.605: Introduction to the History and
11.124: Introduction to Teaching and
11.421: Housing and Human Services
11.981: Graduate Tutorial
1.206: Optimization of Transportation
18.093: Tutoring in Mathematics
17.259: Politics of Race and Ethnicity
22.006: Computer Models of Physical and
22.921: Nuclear Power Plant Dynamics and
9.382: Seminar on Information Processing
11.ThG: Graduate Thesis
24.956: Topics in Syntax
4.254J: Design for Urban Development
6.837: Computer Graphics
1.53: Constructed Facilities Project
18.405J: Advanced Complexity Theory
18.999: Mathematical Reading
14.107: Aquatic Chemistry Laboratory
22.313: Thermal Hydraulics in Nuclear
4.UR: Undergraduate Research in
9.921: Research in Brain and Cognitive
24.518J: Problems of Mental
9.85: Developmental Psychology
12.485: Advanced Directed Field Studies
1.983: Teaching in Civil and Environmental
3.560J: Industrial Ecology
18.062J: Mathematics for Computer Science
11.007J: Controversies in Public Policy
24.951: Introduction to Syntax
9.10: Cognitive Neuroscience
3.082: Materials Processing Laboratory
16.952: Management Topics in Engineering
15.346: Doctoral Seminar in Behavioral and
15.345: Doctoral Seminar in Behavioral and
1.462: Marketing Client-Oriented Services
22.51: Interactions of Radiation
4.689: Preparation for History, Theory, and
16.954J: Research Ethics
22.312: Engineering of Nuclear Reactors
17.211: American Public Policy for
11.438: Economic Development Planning
10.42: Advanced Thermodynamics
16.040: Unified Engineering IV, 12; 16.010, 16.020
13.012: Fluid Mechanics for Ocean
12.722: Special Problems in Chemical
18.735: Topics in Algebra
11.013J: American Urban History |
18.702: Algebra Il
2.792J: Quantitative Physiology: Organ
15.763: The Practice of Operations
24.979: Topics in Semantics
15.678J: Political Economy I: Theories of
11.901: Research Seminar: Topics in Urban
2.890J: Proseminar in Manufacturing
14.103: Dynamic Optimization and
2.183: Biomechanics and Neural Control of
9.373: Somatosensory and Motor
17.208: Comparative Social Policy:
6.046J: Introduction to Algorithms
15.832: Measurement for Management
3.98: Polymer Synthetic Chemistry
6.841J: Advanced Complexity Theory
9.331: Methods in Neural Modeling
8.059: Quantum Physics Ill
10.531: Macromolecular Hydrodynamics
16.422J: Human Supervisory Control of
5.70: Introduction to Statistical
17.105: Political Philosophy
3.83: System Optimization and Analysis for
6.252J: Nonlinear Programming
13.52: Management in Engineering
1.761: Environmental Chemical Kinetics
15.768: Managing Services: Concepts,
8.914: Plasma Astrophysics Il
4.101: Introduction to Architectural Design |
13.665J: Logistical and Transportation
24.ThG: Graduate Thesis
3.931: Industrial Practice
5.73: Introductory Quantum Mechanics |
14.23: Government Regulation of Industry
10.572: Principles of Combustion
4.221: Architecture Studies Faculty
13.999J: Special Projects in Oceanographic
13.015: Mathematical Methods in Ocean
20.921: Selected Topics in Applied
24.950J: Language Acquisition Il
17.267: The President
2.083: Applied Elasticity
16.243: Dynamics of Controlled Structures
15.874: System Dynamics for Business
24.202: Modern Philosophy: Descartes
10.200: Sophomore Advising Seminar
6.630: Electromagnetic Waves
13.78: Entrepreneurship
18.704: Seminar in Algebra and Number
13.615J: Project Control
4.104: Introduction to Architectural Design Il
15.377: R&D Process: Communications and
6.061: Introduction to Electric Power
3.891: Structure and Properties of Materials
16.982: Advanced Special Subject
6.631: Optics and Optical Electronics
15.799: Workshop in Operations
18.336: Numerical Methods of Applied
7.89J: Seminar on Pharmaceutical and
1.67: Sediment Transport and Coastal
15.311: Organizational Processes
6.791: Special Topics in the Solid State and
22.822J: Strategic Analysis for
1.713J: Land-Atmosphere Interaction
15.838: Research Seminar in Marketing
7.08: Molecular Biology
11.941: is taught P/D/F.
12.755: is letter-graded,
13.685J: Manufacturing/Technology
15.073J: Logistical and Transportation
11.220: Quantitative Reasoning and
11.232: The Uses of Social Science for
6.846: Parallel Processing: Systems
7.23: General Immunology
12.337: Tropical Meteorology
15.839: Workshop in Marketing
9.04: Neural Basis of Vision and Audition
16.453J: Human Factors Engineering
15.411: Financial Management
24.910: Topics in Linguistic Theory
5.80: Special Topics in Chemical Physics
10.633: Physicochemical
1.724: Groundwater Modeling
5.561: Chemistry in Industry
43.010: Introduction to Ocean Science and Technology, 12, REST; 8.01, 18.02
1.120: Information Technology M.Eng.
17.510: Language and Politics
10.543J: The Protein Folding Problem
5.68: Kinetics of Chemical Reactions
3.491: Special Problems in Electronic
18.515: Mathematical Logic
2.451J: General Thermodynamics
3.10: Chemical Physics of Materials
16.381: Lasers and Optics for
18.757: Representations of Lie Groups
11.001J: Introduction to Urban Design and
2.182J: Human Supervisory Control of
15.310: Managerial Psychology
3.172: Inventions and Patents
6.345: Automatic Speech Recognition
1.05: Fluid Mechanics
11.463J: Structuring Low-Income Housing
1.69: Introduction to Coastal
22.52J: Statistical Thermodynamics of
1.968: Graduate Studies in Civil and
13.014: Marine Structures and Materials
1.126J: Pattern Recognition and Analysis
15.064J: Engineering Probability and
15.375: New Enterprises
2.03J: Dynamics
8.701: Introduction to Nuclear and Particle
18.023: or 18.02A
3.03: Chemical Metallurgy
4.257J: Property Rights Under Transition
1.89: Environmental Microbiology
4.206: Visualization
9.602J: Language Acquisition Il
11.425: Urban Labor Markets
15.365J: Manufacturing/Technology
9.UR: Undergraduate Research
18.404J: Theory of Computation
17.471: American National Security Policy
10.987: Solid Thin Films and Interfaces
2.96: Management in Engineering
10.UR: Undergraduate Research
5.90: Special Problems in Chemistry
17.541J: Introduction to Latin American
3.563J: Strategic Analysis for
18.745: Introduction to Lie Algebras
22.905: Special Topics in Nuclear
15.930: Strategic Management
6.671: Continuum Electromechanics |
12.221: Geophysical Applications of the
15.951: Special Studies in Management
11.800: Doctoral Research Paper
16.347: Astrodynamics Il
10.977: Process Systems Engineering
12.524: Mechanical Properties of Rocks
7.ThG: Graduate Biology Thesis
6.433: Recursive Estimation
13.742J: Sonar, Radar and Seismic Signal
11.520: A Workshop on Geographic
18.739: Theory of Invariants
6.952: Graduate VI-A Internship
11.360: Community Growth and Land Use
4.237: The New Practitioner: Dialogue Tools
11.367: The Law and Politics of Land Use
22.04: Radiation Effects and Uses
6.951: Graduate VI-A Internship
11.382J: Transit Management
18.337J: Parallel Scientific Computing
1.481: Research Seminar in Construction
18.435J: Theory of Parallel and VLSI
8.513: Many-body Techniques in
18.400J: Automata, Computability, and
15.219: International Management
10.480J: Microelectronics Processing
9.031: Neural Basis of Learning and Memory
7.57J: Genetics and Molecular
5.22J: Biotechnology and Engineering
9.029: Cellular Physiology
3.155J: Microelectronics Processing
16.861: or TPP.21 or 11.200 or 11.205
9.150: Biochemistry and Pharmacology of
9.601J: Language Acquisition |
13.68: Management of Marine Systems
6.435: System Identification
11.361: Environmental Policy and Regulation
6.776J: Plasma Processing in Integrated
18.335J: Numerical Methods of Applied
17.528: Domestic Politics of Trade and
1.142: Civil Engineering Clinic
12.744: Marine Isotope Chemistry
5.14: les of Chemical Selonoe', 12 6.33 Advanced Chemical mentation and
5.50: Enzymes: Structure and Function
6.170: Laboratory in Software Engineering
16.410: Optimization and Decision Analysis
4.299: Special Problems in Architecture
12.864: Ocean Data and Ocean Models |
6.922: Advanced VI-A Internship
6.004: Computation Structures
6.730: Physics for Solid-State
5.24J: Archaeological Science
10.973: Bioengineering
17.403: American Foreign Policy: Past,
6.857: Network and Computer Security
15.952: is taught P/D/F.
1.92: Advanced Civil and Environmental
5.11: Principles of Chemical Science
14.440J: Advanced Financial
18.440: Probability and Random Variables
15.318: Leadership and Change in
17.180J: Institutions for Industrial
18.310: Principles of Applied Mathematics
14.474: Advanced Topics in Public
12.463: Surface Processes and Landscape
6.302: Feedback Systems
17.201J: Controversies in Public Policy
15.231J: Politics and Enterprise in Europe
6.683J: Operation and Planning of Electric
4.253J: Urban Design Politics
2.101: Computer Models of Physical and
4.446: Structures Design Workshop
16.337J: Dynamics of Nonlinear Systems
2.094: Finite Element Analysis of Solids and
2.URG: Undergraduate Research in
2.274: Computational Fluid Dynamics
8.913: Plasma Astrophysics |
6.852J: Distributed Algorithms
11.410J: The Economics of Cities and
6.689: Seminar on Power System Modeling,
3.185: Transport Phenomena in Materials
1.209J: Case Studies in Logistics and
17.302J: Science, Technology, and
13.69: International Shipping
10.991: Seminar in Chemical
16.90: Introduction to Computational
4.269: Special Problems in Social Science
11.125: Observation and Analysis of
12.480: Advanced Igneous Petrology
2.763J: Hyperthermia: Biology,
4.615: The Architecture of Cairo
15.313: Teams in Organizations
8.243: Modern Optics
7.40: Biotechnology: Engineering of
10.974: Catalysis and Reaction Engineering
16.357: Active Control of Fluid Systems
22.03: Engineering of Nuclear Systems
3.902: Special Problems in Polymer Science
12.747: Modeling, Data Analysis, and
17.515: Democracy in Comparative
24.903: Language and its Structure Ill:
22.72J: Corrosion: The Environmental
12.818: Introduction to Atmospheric Data
11.522: Research Seminar on Planning
24.07: Classics in the History of Philosophy
12.806: Atmospheric Physics and
22.928J: Energy in Perspective
1.420: Innovation in Construction
15.960: Special Studies in Management
11.385J: Strategic Analysis for
9.301J: Neural Plasticity in Learning and
22.009: Product-Engineering Process will be offered in 1996-97. It will replace 2.73.
22.55J: Principles of Radiation Applications
4.621: Orientalism and Representation
2.870: Total Quality Development
3.988: Africa — Past and Present: An
6.011: Introduction to Communication,
8.351J: Variational Mechanics: A
13.122: Ship Structural Analysis and
18.126: Functional Analysis
15.563: Inventing the Organizations of the
17.406: Seminar on Middle East Politics
22.092: Engineering Internship
3.90J: Fracture of Structural Materials
6.045J: Automata, Computability, and
16.656: Management Topics in Engineering
1.30: Introduction to Geotechnical
4.499: Special Problems in Building
6.774: Physics of Microelectronic
1.75: Limnology and Wetland Ecology
12.501: Essentials of Geophysics
16.338: Nonlinear Aerospace Control
6.262: Discrete Stochastic Processes
18.755: Introduction to Lie Groups
17.URG: Undergraduate Research
3.55: Macroscopic Transport in Materials
13.021: Marine Hydrodynamics |
15.355: Managing Technological
2.72: Elements of Mechanical Design
11.471: Political Economy of Development
15.676: Industrial Relations Theory and
3.URG: Undergraduate Research
2.671: Measurement and Instrumentation
17.405: Seminar on Middle East Politics
8.510J: Application of Group Theory to the
9.100: Cognitive Neuroscience
1.207: Models and Algorithms for
9.594: —Psycholinguistics, 12; 9.62"
6.014: Electrodynamics
13.111: Structural Mechanics
18.024: Calculus with Theory
18.395: Group Theory with Applications to
8.532: Modern Topics in Solid State
11.331J: Advanced Seminar in City Form
12.616: Occultation Studies of the Solar
14.ThG: Graduate Thesis
18.950: Differential Geometry
22.82: Engineering Risk-Benefit Analysis
4.623: Technology and the Modern Project
12.570: is letter-graded.
13.50: Numerical Methods with Applications
4.23J: Special Interest Group in Urban
17.258: Politics of Race and Ethnicity
24.902: Language and its Structure Il: Syntax
8.324: Relativistic Quantum Field
22.102: Engineering Principles for Nuclear
6.245: Multivariable Control Systems
13.25J: Thermal Power Engineering
9.359J: Special Topics in Vision Science
9.09J: Cellular Neurobiology
8.422: Atomic and Optical Physics Il
4.245J: Cities of Tomorrow
10.341: Finite Element Methods for
12.457: Sedimentary Basins
13.661: Economics of Marine Transportation

New subjects introduced by 2024:
20.365: Engineering the Immune System in Cancer and Beyond
22.EPW: UPOP Engineering Practice Workshop
3.086: Innovation and Commercialization of Materials Technology
7.45: The Hallmarks of Cancer
20.101: Metakaryotic Biology and Epidemiology
20.102: Metakaryotic Stem Cells in Carcinogenesis: Origins and Cures
24.503: Topics in Philosophy of Religion
3.033: Electronic, Optical and Magnetic Properties of Materials
2.013: Engineering Systems Design
10.677: Topics in Applied Microfluidics
18.0651: Matrix Methods in Data Analysis, Signal Processing, and Machine Learning
12.349: Mechanisms and Models of the Global Carbon Cycle
2.00B: Toy Product Design
7.S939: Special Subject in Biology
11.142: Geography of the Global Economy
2.019: Design of Ocean Systems
24.420: Ancient Philosophy
17.178: Political Economy of Institutions and Development
12.372: Elements of Modern Oceanography
18.408: Topics in Theoretical Computer Science
11.100: Introduction to Computational Thinking in Cities
10.22: Molecular Engineering
1.037: Soil Mechanics and Geotechnical Design
7.935: Responsible Conduct in Biology
5.383: Fast-flow Peptide and Protein Synthesis
11.107: Economic Development Planning and Policy
8.10: Exploring and Communicating Physics (and other) Frontiers
11.158: Behavioral Science, AI, and Urban Mobility
12.TIP: Thesis Preparation
8.251: String Theory for Undergraduates
20.409: Biological Engineering II: Instrumentation and Measurement
6.100B: Introduction to Computational Thinking and Data Science
4.105: Cultures of Form
4.022: Introduction to Architectural Design Techniques
12.00: Frontiers and Careers in Earth, Planets, Climate, and Life
1.021: Introduction to Modeling and Simulation
12.390: Fluid Dynamics of the Atmosphere and Ocean
24.121: Metaphysics
11.137: Financing Economic Development and Housing
24.504: Topics in Aesthetics
5.49: Chemical Microbiology
6.5660: Computer Systems Security
6.5320: Geometric Computing
10.51: Nanoscale Energy Transport Processes
1.052: Advancing Mechanics and Materials via Machine Learning
16.301: Topics in Control, Dynamics, and Automation
15.071: The Analytics Edge
10.492B: Integrated Chemical Engineering Topics I
8.277: Introduction to Particle Accelerators
7.THG: Graduate Biology Thesis
24.133: Experiential Ethics
6.5310: Geometric Folding Algorithms: Linkages, Origami, Polyhedra
16.120: Compressible Internal Flow
2.121: Stochastic Systems
17.181: Sustainability: Political Economy, Science, and Policy
15.014: Applied Macro- and International Economics II
20.450: Applied Microbiology
24.THG: Graduate Thesis
11.138: Crowd Sourced City: Civic Tech Prototyping
22.EPE: UPOP Engineering Practice Experience
18.100Q: Real Analysis
3.16: Industrial Challenges in Metallic Materials Selection
8.295: Practical Experience in Physics
12.318: Introduction to Atmospheric Data and Large-scale Dynamics
8.224: Exploring Black Holes: General Relativity and Astrophysics
15.097: Seminar in Statistics and Data Analysis
14.387: Applied Econometrics
4.S15: Special Subject: Design
22.072: Corrosion: The Environmental Degradation of Materials
7.C51: Machine Learning in Molecular and Cellular Biology
10.04: A Philosophical History of Energy
17.031: American Political Thought
17.279: Political Misinformation in the Age of Social Media
7.094: Modern Computational Biology
18.4531: Combinatorial Optimization
4.041: Design Studio: Advanced Product Design
4.110: Design Across Scales and Disciplines
8.241: Introduction to Biological Physics
20.352: Principles of Neuroengineering
4.151: Architecture Design Core Studio I
2.145: Design of Compliant Mechanisms, Machines and Systems
15.275: Creative Industries: Media, Entertainment, and the Arts (New)
5.069: Crystal Structure Analysis
7.24: Advanced Concepts in Immunology
12.177: Astrobiology, Origins and Early Evolution of Life
3.052: Nanomechanics of Materials and Biomaterials
11.159: Entrepreneurial Negotiation
20.375: Applied Developmental Biology and Tissue Engineering
4.123: Architectural Assemblies
7.345-7.349: Advanced Undergraduate Seminar
16.32: Principles of Optimal Control and Estimation
17.265: Public Opinion and American Democracy
6.5150: Large-scale Symbolic Systems
3.003: Small Planet Engineering: Climate, Energy, and Sustainability
4.043: Design Studio: Interaction Intelligence
7.75: Human Genetics and Genomics
1.032: Advanced Soil Mechanics
12.010: Computational Methods of Scientific Programming
11.149: Decarbonizing Urban Mobility
4.109: Materials and Fabrication for Architecture
17.307: American Public Policy for Washington Interns
11.S196-11.S199: Special Subject: Urban Studies and Planning
7.574: Modern Computational Biology
3.046: Advanced Thermodynamics of Materials
9.360: Neurobiology of Self
11.191-11.192: Independent Study
10.494B: Integrated Chemical Engineering Topics III
2.184: Biomechanics and Neural Control of Movement
7.00: COVID-19, SARS-CoV-2 and the Pandemic
11.145: International Housing Economics and Finance
4.S11: Special Subject: Architecture Design
16.530: Advanced Propulsion Concepts
18.100B: Real Analysis
20.920: Practical Work Experience
17.263: Electoral Politics, Public Opinion, and Democracy
14.399: Seminar in Data Economics and Development Policy
8.09: Classical Mechanics III
15.089: Analytics Capstone
11.S04: Special Subject: Topics in Affordable Housing
15.226: Modern Business in Southeast Asia: ASEAN Lab
17.156: Welfare and Capitalism in Western Europe
20.213: Genome Stability and Engineering in the Context of Diseases, Drugs, and Public Health
20.265: Genetics for Biological Engineering
18.0751: Methods for Scientists and Engineers
4.02A: Design Studio: How to Design Intensive
24.220: Moral Psychology
7.80: Fundamentals of Chemical Biology
14.147: Topics in Game Theory
12.385: Science, Politics, and Environmental Policy
14.283: Advanced Topics in Organizational Economics I
12.377: The History of Earth's Climate
17.200: American Political Behavior I
15.002: Leadership Challenges for an Inclusive World
5.111: Principles of Chemical Science
5.362: Cancer Drug Efficacy
10.345: Fundamentals of Metabolic and Biochemical Engineering: Applications to Biomanufacturing
18.1011: Analysis and Manifolds
24.130: Ethics
6.5120: Formal Reasoning About Programs
6.5930: Hardware Architecture for Deep Learning
3.321: Computational Materials Design
24.09: Minds and Machines
6.5430: Quantum Complexity Theory
15.277: Seminar in Communications
12.373: Field Oceanography
4.193: Independent Study in Architecture Design
24.URG: Undergraduate Research
4.S03: Special Subject: Design
2.155: Artificial Intelligence and Machine Learning for Engineering Design
17.154: Varieties of Capitalism and Social Inequality
15.1411: Economics of Health Care Industries
5.373: Synthesis of Boron Heterocycles
16.235: Design with High Temperature Materials
2.154: Maneuvering and Control of Surface  and Underwater Vehicles
10.495: Molecular Design and Bioprocess Development of Immunotherapies
2.095: Introduction to Finite Element Methods
18.0861: Computational Science and Engineering II
12.021: Earth Science, Energy, and the Environment
16.001: Unified Engineering: Materials and Structures
20.903: Independent Study in Biological Engineering
10.000: Engineering Molecular Marvels:  Careers and ChemE at MIT
18.3541: Nonlinear Dynamics: Continuum Systems
6.5931: Hardware Architecture for Deep Learning
21.01: Compass Course: Moral and Social Questions about the Human Condition (New)
24.222: Decisions, Games and Rational Choice
10.489: Concepts in Modern Heterogeneous Catalysis
22.003: NEET Seminar: Renewable Energy Machines
24.636: Topics in Social Theory and Practice
24.602: Topics in the Philosophy of Agency
1.050: Solid Mechanics
17.100: Field Seminar in Political Economy
6.1020: Software Construction
5.363: Organic Structure Determination
10.06: Advanced Topics in Ethics for Engineers
7.393: Independent Study in Genetics
12.THU: Undergraduate Thesis
11.S195: Special Subject: Urban Studies and Planning
6.5950: Secure Hardware Design
7.31: Current Topics in Mammalian Biology: Medical Implications
10.466: Structure of Soft Matter
2.065: Acoustics and Sensing
20.051: Introduction to NEET: Living Machines
20.202: In vivo Models: Principles and Practices
14.19: Market Design
6.5060: Algorithm Engineering
3.001: Science and Engineering of Materials
14.150: Networks
1.063: Fluids and Diseases
5.353: Macromolecular Prodrugs
24.230: Meta-ethics
18.300: Principles of Continuum Applied Mathematics
16.485: Visual Navigation for Autonomous Vehicles
11.006: Poverty and Economic Security
Core: and General Science Subjects
8.S271: Special Subject:  Physics
6.1850: Computer Systems and Society
4.181: Architectural Design Workshop
4.090: Practical Experience in Architecture for Undergraduates
15.283: Social Media Management: Persuasion in Networked Culture
18.0851: Computational Science and Engineering I
15.087: Engineering Statistics and Data Science
8.228: Relativity II
20.EPE: UPOP Engineering Practice Experience
3.202: Essential Research Skills
11.148: Environmental Justice: Law and Policy
9.17: Systems Neuroscience Laboratory
4.021: Design Studio: How to Design
4.183-4.185: Architectural Design Workshop
2.00A: Designing for the Future: Earth, Sea, and Space
9.190: Computational Psycholinguistics
6.1040: Software Design
1.088: Genomics and Evolution of Infectious Disease
Graduate: Subjects
Geology: and Geochemistry
22.001: Introduction to Undergraduate Research I (New)
2.086: Numerical Computation for Mechanical Engineers
24.236: Topics in Social Theory and Practice
20.950: Research Problems in Biological Engineering
22.06: Engineering of Nuclear Systems
4.182: Architectural Design Workshop
6.120A: Discrete Mathematics and Proof for Computer Science
5.064: Solid-state Materials Chemistry
15.227: - 15.229 Seminar in International Management
22.022: Quantum Technology and Devices
3.156: Photonic Materials and Devices
6.1420: Fixed Parameter and Fine-grained Computation
6.5910: Complex Digital Systems Design
14.27: Economics and E-Commerce
7.573: Modern Biostatistics
10.626: Electrochemical Energy Systems
18.413: Introduction to Computational Molecular Biology
14.39: Large-Scale Decision-Making and Inference (New)
16.363: Communication Systems and Networks
1.089: Environmental Microbial Biogeochemistry
6.1800: Computer Systems Engineering
18.100P: Real Analysis
14.197: Independent Research
20.473: Foundations of Cell Therapy Manufacturing
20.475: Applied Developmental Biology and Tissue Engineering
4.053: Visual Communication Fundamentals
14.38: Inference on Causal and Structural Parameters Using ML and AI
6.1060: Software Performance Engineering
4.093: Independent Study in Design
10.28A: Chemical-Biological Engineering Laboratory I: Introduction to Lab Experiments
4.118: Creative Computation
3.004: Small Planet Engineering: Climate, Energy, and Sustainability
24.013: Philosophy and the Arts
15.0711: The Analytics Edge
18.118: Topics in Analysis
14.16: Strategy and Information
22.099: Topics in Nuclear Science and Engineering
2.066: Acoustics and Sensing
12.110A: Sedimentary Environments
11.193-11.194: Supervised Readings
4.S10: Special Subject: Architecture Design
18.137: Topics in Geometric Partial Differential Equations
7.470: Biological Oceanography
3.013: Mechanics of Materials
1.104: Sensing and Intelligent Systems
16.201: Topics in Materials and Structures
15.230: Public Policy and the Private Sector
3.006: NEET Seminar: Advanced Materials Machines
2.009: The Product Engineering Process
7.494: Research Problems in Microbiology
9.014: Quantitative Methods and Computational Models in Neurosciences
9.32: Genes, Circuits, and Behavior
20.054: NEET - Living Machines Research Immersion
14.310: Data Analysis for Social Scientists
6.100A: Introduction to Computer Science Programming in Python
14.32: Econometric Data Science
5.382: Time- and Frequency-resolved Spectroscopy of Photosynthesis
9.36: Neurobiology of Self
2.S02: Special Subject in Mechanical Engineering
8.EPE: UPOP Engineering Practice Experience
8.06: Quantum Physics III
16.S685: Special Subject in Aeronautics and Astronautics
18.091: Introduction to Metric Spaces (New)
14.009: Economics and Society's Toughest Problems
14.388: Inference on Causal and Structural Parameters Using ML and AI
6.5840: Distributed Computer Systems Engineering
24.201: Topics in the History of Philosophy
10.586: Crystallization Science and Technology
3.080: Strategic Materials Selection
15.025: Game Theory for Strategic Advantage
4.S02: Special Subject: Design
Independent: Research Subjects
10.08: Cultural Studies for Chemical Engineering Graduate Students
9.017: Systems Neuroscience Core II
10.424: Pharmaceutical Engineering
10.443: Future Medicine: Drug Delivery, Therapeutics, and Diagnostics
1.060: Fluid Mechanics
1.005: Experiential Sustainability
18.1001: Real Analysis
12.012: MatLab, Statistics, Regression, Signal Processing
15.027: Opportunities in Developing Economies
6.1904: Introduction to Low-level Programming in C and Assembly
14.270: Economics and E-Commerce
11.139: The City in Film
7.58: Molecular Biology
3.010: Structure of Materials
6.5831: Database Systems
18.424: Seminar in Information Theory
7.38: Design Principles of Biological Systems
9.490: Neural Circuits for Cognition
24.93: The Search for Meaning
10.02: Foundations of Entrepreneurship for Engineers
11.154: Big Data, Visualization, and Society
20.S952: Special Subject in Biological Engineering
15.285: Sports Strategy and Analytics
11.074: Cybersecurity Clinic
16.004: Unified Engineering: Thermodynamics and Propulsion
11.171: Indigenous Environmental Planning
5.112: Principles of Chemical Science
6.1120: Dynamic Computer Language Engineering
7.498: Teaching Experience in Microbiology
10.689: Concepts in Modern Heterogeneous Catalysis
14.18: Mathematical Economic Modeling
6.1100: Computer Language Engineering
7.28: Molecular Biology
24.191: Being, Thinking, Doing (or Not): Ethics in Your Life
20.S948: Special Subject in Biological Engineering
6.1810: Operating System Engineering
24.223: Rationality
14.33: Research and Communication in Economics: Topics, Methods, and Implementation
2.180: Biomolecular Feedback Systems
2.132: Instrumentation and Measurement: MICA Projects (New)
3.19: Sustainable Chemical Metallurgy
3.096: Architectural Ironwork
20.020: Introduction to Biological Engineering Design Using Synthetic Biology
7.S932: Special Subject in Biology
14.281: Contract Economics
11.135: Violence, Human Rights, and Justice
10.493: Integrated Chemical Engineering Topics II
11.S187: Special Subject: Urban Studies and Planning
12.170: Essentials of Geology
16.332: Formal Methods for Safe Autonomous Systems
5.39: Research and Communication in Chemistry
7.MTHG: Microbiology Graduate Thesis
6.5920: Parallel Computing
1.006: Tools for Sustainable Design
14.131: Psychology and Economics
15.225: Modern Business in China: China Lab
20.005: Ethics for Engineers
2.147: Design of Compliant Mechanisms, Machines and Systems
18.397: Mathematical Methods in Physics
7.016: Introductory Biology
5.381: Quantum Dots
17.150: The American Political Economy in Comparative Perspective
14.195: Reading Seminar in Economics
15.0341: Econometrics for Managers: Correlation and Causality in a Big Data World
20.460: Computational Analysis of Biological Data
24.245: Theory of Models
5.301: Chemistry Laboratory Techniques
24.635: Topics in Critical Social Theory
6.5110: Foundations of Program Analysis
15.278: Seminar in Communications
24.634: Global Justice, Gender, and Development
3.044: Materials Processing
18.212: Algebraic Combinatorics
14.36: Advanced Econometrics
2.110: Information, Entropy, and Computation
6.5850: Principles of Computer Systems
15.003: Analytics Tools
22.C01: Modeling with Machine Learning: Nuclear Science and Engineering Applications
20.BME: Undergraduate Research in Biomedical Engineering
6.5951: Secure Hardware Design
4.033: Design Studio: Information Design and Visualization
6.5420: Randomness and Computation
12.178: The Phylogenomic Planetary Record
3.017: Modelling, Problem Solving, Computing, and Visualization
3.17: Principles of Manufacturing
22.052: Quantum Theory of Materials Characterization
8.S227: Special Subject:  Physics
11.147: Budgeting and Finance for the Public Sector
4.152: Architecture Design Core Studio II
17.03: Introduction to Political Thought
2.082: Ship Structural Analysis and Design
4.192: Independent Study in Architecture Design
10.10: Introduction to Chemical Engineering
16.420: Planning Under Uncertainty
18.204: Undergraduate Seminar in Discrete Mathematics
14.282: Introduction to Organizational Economics
7.390: Practical Internship Experience in Biology
20.315: Physical Biology
6.5830: Database Systems
6.5230: Advanced Data Structures
3.039: Mathematics and Computational Thinking for Materials Scientists and Engineers II
20.260: Computational Analysis of Biological Data
9.49: Neural Circuits for Cognition
9.40: Introduction to Neural Computation
12.000: Solving Complex Problems
7.340-7.344: Advanced Undergraduate Seminar
2.18: Biomolecular Feedback Systems
18.022: Calculus
Introductory: Biology
7.933: Research Rotations in Biology
2.016: Hydrodynamics
10.29: Biological Engineering Projects Laboratory
4.031: Design Studio: Objects and Interaction
1.073: Introduction to Environmental Data Analysis
2.014: Engineering Systems Development
2.168: Learning Machines
6.5610: Applied Cryptography and Security
8.S30: Special Subject:  Physics
22.051: Systems Analysis of the Nuclear Fuel Cycle
7.35: Human Genetics and Genomics
24.213: Philosophy of Film
18.225: Graph Theory and Additive Combinatorics
18.032: Differential Equations
16.36: Communication Systems and Networks
4.094: Independent Study in Design
22.01: Introduction to Nuclear Engineering and Ionizing Radiation
16.07: Dynamics
17.389: Education, Inequality, and Politics
20.902: Independent Study in Biological Engineering
14.300: Introduction to Statistical Methods in Economics
10.56: Advanced Topics in Surfactant Science
2.120: Introduction to Robotics
4.S13: Special Subject: Architecture Design
12.391: Current Topics in Earth, Atmospheric and Planetary Sciences
9.357: Current Topics in Perception
15.218: Global Economic Challenges and Opportunities
4.092: Independent Study in Design
18.404: Theory of Computation
18.102: Introduction to Functional Analysis
22.071: Analog Electronics and Analog Instrumentation Design
11.S189: Special Subject: Urban Studies and Planning
3.207: Innovation and Commercialization
10.321: Design Principles in Mammalian Systems and Synthetic Biology
11.THU: Undergraduate Thesis
12.007: Geobiology: History of Life on Earth
7.571: Quantitative Analysis of Biological Data
22.039: Integration of Reactor Design, Operations, and Safety
15.276: Communicating with Data
22.015: Radiation and Life: Applications of Radiation Sources in Medicine, Research, and Industry
2.156: Artificial Intelligence and Machine Learning for Engineering Design
7.32: Systems Biology
4.044: Design Studio: Interaction Intelligence
20.560: Statistics for Biological Engineering
12.086: Modeling Environmental Complexity
11.027: City to City: Comparing, Researching, and Reflecting on Practice
11.119: NEET Seminar: Digital Cities
15.270: Ethical Practice:  Leading Through Professionalism, Social Responsibility, and System Design
16.002: Unified Engineering: Signals and Systems
2.S00: Special Subject in Mechanical Engineering
7.430: Topics in Quantitative Marine Science
7.C01: Machine Learning in Molecular and Cellular Biology
3.201: Introduction to DMSE
7.440: An Introduction to Mathematical Ecology
10.09: Models of Molecular Systems: from Newtonian Mechanics to Machine Learning
15.000: Explorations in Management
2.S01: Special Subject in Mechanical Engineering
11.113: The Economic Approach to Cities and Environmental Sustainability
16.S684: Special Subject in Aeronautics and Astronautics
3.002: Materials for Energy and Sustainability
6.1010: Fundamentals of Programming
14.163: Algorithms and Behavioral Science
14.284: Advanced Topics in Organizational Economics II
5.372: Chemistry of Renewable Energy
12.306: Atmospheric Physics and Chemistry
7.66: Molecular Basis of Infectious Disease
7.394: Independent Study in Biochemistry
7.410: Applied Statistics
20.381: Biological Engineering Design II
24.116: Philosophy of Statistics
6.5900: Computer System Architecture
Microbiology: (MICRO)
18.1002: Real Analysis
15.095: Machine Learning Under a Modern Optimization Lens
12.225: Mechanisms of Faulting and Earthquakes (New)
16.422: Human Supervisory Control of Automated Systems
12.117A: Field Geobiology I
8.223: Classical Mechanics II
3.171: Structural Materials and Manufacturing
5.361: Recombinant DNA Technology
1.060A: Fluid Mechanics I
12.12: Nature's Sandbox: The History of Ancient Environments, Climate, and Life
5.351: Fundamentals of Spectroscopy
7.433: Topics in Biological Oceanography
6.5630: Advanced Topics in Cryptography
14.130: Reading Economic Theory
3.023: Synthesis and Design of Materials
10.353: Model Predictive Control
7.86: Building with Cells
24.134: Experiential Ethics
24.234: Global Justice, Gender, and Development
6.5340: Topics in Algorithmic Game Theory
3.000: Coffee Matters: Using the Breakerspace to Make the Perfect Cup
16.401: Topics in Communication and Software
10.591: Case Studies in Bioengineering
5.067: Crystal Structure Refinement
9.13: The Human Brain
1.004: Startup Sustainable Tech
22.S092-22.S094: Special Subject in Nuclear Science and Engineering
9.41: Research and Communication in Neuroscience and Cognitive Science
4.180: Design Workshop
2.087: Engineering Mathematics: Linear Algebra and ODEs
3.088: The Social Life of Materials
21.THU: Undergraduate Thesis in Humanities
1.074: Multivariate Data Analysis
22.074: Radiation Damage and Effects in Nuclear Materials
4.125: Furniture Making Workshop
15.005: Sloan Intensive Period Elective Requirement
14.000: Graduate Internship in Economics
3.18: Materials Science and Engineering of Clean Energy
2.077: Solid Mechanics: Coupled Theories
24.502: Topics in Metaphysics and Ethics
9.24: Disorders and Diseases of the Nervous System
20.380: Biological Engineering Design
6.5081: Multicore Programming
2.16: Learning Machines
15.0621: Data Mining: Finding the Models and Predictions that Create Value
4.153: Architecture Design Core Studio III
18.226: Probabilistic Methods in Combinatorics
24.S41: Special Seminar: Philosophy
18.367: Waves and Imaging
8.298: Selected Topics in Physics
1.072: Groundwater Hydrology
1.068: Nonlinear Dynamics and Turbulence
14.08: Technical Topics in Economics
16.S686: Special Subject in Aeronautics and Astronautics
17.20: Introduction to the American Political Process
16.EPW: UPOP Engineering Practice Workshop
1.057: Heritage Science and Technology
3.23: Electrical, Optical, and Magnetic Properties of Materials
24.141: Logic I
14.320: Econometric Data Science
20.UR: Undergraduate Research Opportunities
10.28B: Chemical-Biological Engineering Laboratory II: Long-term, Online and Simulated Experiments
24.S40: Special Seminar: Philosophy
4.154: Architecture Design Option Studio
12.420: Essentials of Planetary Science
11.008: Undergraduate Planning Seminar
16.470: Statistical Methods in Experimental Design
12.422: Planetary Atmospheres
20.S947: Special Subject in Biological Engineering
5.065: Electrochemistry
6.1920: Constructive Computer Architecture
16.18: Fundamentals of Turbulence
3.030: Microstructural Evolution in Materials
17.174: Historical Political Economy
22.00: Introduction to Modeling and Simulation
7.392: Independent Study in Biology
4.120: Furniture Making Workshop
2.131: Advanced Instrumentation and Measurement
24.251: Introduction to Philosophy of Language
6.1903: Introduction to Low-level Programming in C and Assembly
9.012: Cognitive Science
18.200A: Principles of Discrete Applied Mathematics
16.391: Statistics for Engineers and Scientists
24.893: Dissertation Workshop
8.051: Quantum Physics II
7.S391: Special Subject in Biology
17.320: Social Policy
17.270: American Political Development
20.THG: Graduate Thesis
18.453: Combinatorial Optimization
24.899: Topics in Linguistics and Philosophy
2.12: Introduction to Robotics
6.100L: Introduction to Computer Science and Programming
20.109: Laboratory Fundamentals in Biological Engineering
3.042: Materials Project Laboratory
20.490: Computational Systems Biology: Deep Learning in the Life Sciences
12.096: Current Topics in Atmospheric Science and Oceanography
7.46: Building with Cells
1.009: Climate Change
17.198: Current Topics in Comparative Political Economy
18.211: Combinatorial Analysis
Planetary: Science and Astronomy
18.090: Introduction to Mathematical Reasoning
24.253: Philosophy of Mathematics
7.936: Professional Development in Biology
16.501: Topics in Propulsion
15.287: Communication and Persuasion Through Data
12.117B: Field Geobiology II
6.5810: Operating System Engineering
4.S01: Special Subject: Design
10.00: Molecule Builders
11.041: Introduction to Housing, Community, and Economic Development
10.524: Pharmaceutical Engineering
15.216: Central Banks, Monetary Policy and Global Financial Markets
20.945: Practical Experience in Biological Engineering
8.041: Quantum Physics I
15.288: Tough Conversations
18.200: Principles of Discrete Applied Mathematics
10.426: Electrochemical Energy Systems
14.161: Strategy and Information
2.140: Analysis and Design of Feedback Control Systems
6.5240: Sublinear Time Algorithms
18.218: Topics in Combinatorics
3.173: Computing Fabrics
3.22: Structure and Mechanics of Materials
10.492A: Integrated Chemical Engineering Topics I
Undergraduate: Seminars
3.071: Amorphous Materials
20.S901: Special Subject in Biological Engineering
20.951: Thesis Proposal
11.140: Urbanization and Development
22.S095: Special Subject in Nuclear Science and Engineering
7.572: Quantitative Measurements and Modeling of Biological Systems
14.35: Why Markets Fail
24.894: Placement Workshop
11.143: Research Methods in Global Health and Development
1.086: Physics of Renewable Energy Systems and Computational Analysis
20.219: Selected Topics in Biological Engineering
1.091: Traveling Research Environmental eXperience (TREX): Fieldwork
8.S02: Special Subject:  Physics
16.003: Unified Engineering: Fluid Dynamics
1.010: Probability and Causal Inference
15.286: Communicating with Data
10.553: Model Predictive Control
7.S399: Special Subject in Biology
20.465: Engineering the Immune System in Cancer and Beyond
8.THU: Undergraduate Physics Thesis
14.11: Topics in Economics
1.080: Environmental Chemistry
4.S12: Special Subject: Architecture Design
20.THU: Undergraduate BE Thesis
2.004: Dynamics and Control II
8.S014: Special Subject: Physics (New)
11.170: Cities and Climate Change: Mitigation and Adaptation
24.233: The Ethics of Climate Change
5.302: Introduction to Experimental Chemistry
24.S00: Special Subject: Philosophy
6.5080: Multicore Programming
16.395: Principles of Wide Bandwidth Communication
3.087: Materials, Societal Impact, and Social Innovation
7.934: Teaching Experience in Biology
10.352: Modern Control Design
1.097: Introduction to Civil and Environmental Engineering Research
8.S50: Special Subject:  Physics
10.566: Structure of Soft Matter
4.023: Architecture Design Studio I
14.273: Advanced Topics in Industrial Organization
15.004: Programming for Finance Professionals
15.248: MENA Lab: Promoting Innovation & Entrepreneurship in the Middle East and North Africa
20.415: Physical Biology
14.13: Psychology and Economics
1.008: Engineering for a Sustainable World
11.S03: Special Subject: Transportation Shaping Sustainable Urbanization: Connections with Behavior, Urban Economics and Planning
10.595: Molecular Design and Bioprocess Development of Immunotherapies
12.315: Atmospheric Radiation and Convection
12.110B: Sedimentology in the Field
1.035: Mechanics of Materials
8.006: Exploring Physics Using Python (New)
18.065: Matrix Methods in Data Analysis, Signal Processing, and Machine Learning
7.S930: Special Subject in Biology
1.020: Modeling and Decision-Making for Sustainability
12.202: Flow, Deformation, and Fracture in Earth and Other Terrestrial Bodies
8.226: Forty-three Orders of Magnitude
7.371: Biological and Engineering Principles Underlying Novel Biotherapeutics
4.190: Practical Experience in Architecture
17.315: Health Policy
9.07: Statistics for Brain and Cognitive Science
18.1021: Introduction to Functional Analysis
7.395: Independent Study in Cell and Molecular Biology
7.83: Design Principles of Biological Systems
12.211: Field Geophysics
21.00: SHASS Exploration
11.156: Healthy Cities: Assessing Health Impacts of Policies and Plans
18.100A: Real Analysis
18.455: Advanced Combinatorial Optimization
4.024: Architecture Design Studio II
9.42: The Brain and Its Interface with the Body
2.075: Mechanics of Soft Materials
1.076: Carbon Management
11.092: Renewable Energy Facility Siting Clinic
6.1210: Introduction to Algorithms
7.102: Introduction to Molecular Biology Techniques
8.021: Physics II
6.5350: Matrix Multiplication and Graph Algorithms
15.015: Macroeconomic Policy Reforms
3.098: Ancient Engineering: Ceramic Technologies
21.THT: Humanities Pre-Thesis Tutorial
14.003: Microeconomic Theory and Public Policy
14.390: Large-Scale Decision-Making and Inference (New)
10.585: Engineering Nanotechnology
3.009: Materials, Mechanics, and Flight: Birds, an Engineer?s Delight
2.122: Stochastic Systems
6.5820: Computer Networks
10.28: Chemical-Biological Engineering Laboratory
8.S199: Special Subject: Physics (New)
11.144: Project Appraisal in Developing Countries
22.C51: Modeling with Machine Learning: Nuclear Science and Engineering Applications
7.26: Molecular Basis of Infectious Disease
2.071: Mechanics of Solid Materials
3.019: Introduction to Symbolic and Mathematical Computing
7.411: Seminars in Biological Oceanography
20.215: Macroepidemiology, Population Genetics, and Stem Cell Biology of Human Clonal Diseases
20.URG: Undergraduate Research Opportunities
22.S097: Special Subject in Nuclear Science and Engineering
2.00: Introduction to Design
2.133: Instrumentation and Measurement: MICA Projects (New)
20.960: Teaching Experience in Biological Engineering
7.932: Independent Study in Biology
16.06: Principles of Automatic Control
17.276: Public Opinion Research Training Lab
18.063: Matrix Calculus for Machine Learning and Beyond (New)
10.494A: Integrated Chemical Engineering Topics III
22.016: Seminar in Fusion and Plasma Physics
3.074: Imaging of Materials
15.284: Strategic Leadership Communication
7.36: The CRISPR Revolution:  Engineering the Genome for Basic Science and Clinical Medicine (New)
18.217: Combinatorial Theory
4.091: Independent Study in Design
3.021: Introduction to Modeling and Simulation
MIT-WHOI: Joint Program in Oceanography
16.35: Real-Time Systems and Software
18.1121: Functions of a Complex Variable
7.093: Modern Biostatistics
15.0251: Game Theory for Strategic Advantage
20.S949: Special Subject in Biological Engineering
18.1521: Introduction to Partial Differential Equations
24.132: Workshop in Ethical Engineering
17.055: Just Code: The Ethical Lifecycle of Machine Learning
18.338: Eigenvalues of Random Matrices
14.160: Behavioral Economics
6.5940: TinyML and Efficient Deep Learning Computing
1.082: Ethics for Engineers
1.000: Introduction to Computer Programming and Numerical Methods for Engineering Applications
3.157: Organic Electronic Materials and Devices (New)
22.THT: Undergraduate Thesis Tutorial
1.010A: Probability: Concepts and Applications
1.061A: Transport Processes in the Environment I
7.499: Research Rotations in Microbiology
20.373: Foundations of Cell Therapy Manufacturing
1.010B: Causal Inference for Data Analysis
1.077: Land, Water, Food, and Climate
9.19: Computational Psycholinguistics
18.1031: Fourier Analysis: Theory and Applications
7.55: Case Studies in Modern Experimental Design
7.S392: Special Subject in Biology
10.05: Foundational Analyses of Problems in Energy and the Environment
20.EPW: UPOP Engineering Practice Workshop
4.S14: Special Subject: Architecture Design
7.396: Independent Study in Experimental Biology
8.011: Physics I
3.029: Mathematics and Computational Thinking for Materials Scientists and Engineers I
5.352: Synthesis of Coordination Compounds and Kinetics
15.110: Operations Research Experience Internship
14.200: Industrial Organization: Competitive Strategy and Public Policy
20.S900: Special Subject in Biological Engineering
6.5151: Large-scale Symbolic Systems
1.075: Water Resource Systems
11.189-11.190: Urban Fieldwork
1.022: Introduction to Network Models
20.334: Biological Systems Modeling
20.001: Introduction to Professional Success and Leadership in Biological Engineering
14.001: Data Economics and Development Policy Summer Internship
7.015: Introductory Biology
6.1910: Computation Structures
3.054: Cellular Solids: Structure, Properties, Applications
12.080: Experiential Learning in EAPS
16.S688: Special Subject in Aeronautics and Astronautics
4.051: The Human Factor in Innovation and Design Strategy
22.017: Nuclear in the News
15.0111: Economic Analysis for Business Decisions
18.434: Seminar in Theoretical Computer Science
1.036: Structural Mechanics and Design
9.011: Systems Neuroscience Core I
11.169: Global Climate Policy and Sustainability
17.317: US Social Policy
16.EPE: UPOP Engineering Practice Experience
5.371: Continuous Flow Chemistry:  Sustainable Conversion of Reclaimed Vegetable Oil into Biodiesel
17.115: International Political Economy
20.345: Bioinstrumentation Project Lab
11.S188: Special Subject: Urban Studies and Planning
10.333: Introduction to Modeling and Simulation
4.117: Creative Computation
18.031: System Functions and the Laplace Transform
16.393: Statistical Communication and Localization Theory
3.152: Magnetic Materials
24.131: Ethics of Technology
20.440: Analysis of Biological Networks
12.210: Introduction to Seismology (New)
16.475: Human-Computer Interface Design Colloquium
20.385: Design in Synthetic Biology
10.544: Metabolic and Cell Engineering
1.061: Transport Processes in the Environment
11.005: Introduction to International Development
7.S931: Special Subject in Biology
11.166: Law, Social Movements, and Public Policy: Comparative and International Experience
16.101: Topics in Fluids
14.00: Undergraduate Internship in Economics
2.098: Introduction to Finite Element Methods
7.931: Independent Study in Biology
2.000: Explorations in Mechanical Engineering
24.215: Topics in the Philosophy of Science
7.62: Microbial Physiology
14.260: Organizational Economics
16.30: Feedback Control Systems
1.101: Introduction to Civil and Environmental Engineering Design I
15.090: Common Experience in Operations Research
10.01: Ethics for Engineers
14.380: Statistical Method in Economics
24.252: Language and Power
1.058: Structural Dynamics
18.219: Seminar in Combinatorics
14.192: Advanced Research and Communication
10.552: Modern Control Design
2.14: Analysis and Design of Feedback Control Systems
1.013: Senior Civil and Environmental Engineering Design
12.307: Weather and Climate Laboratory
24.410: Topics in the History of Philosophy
20.200: Biological Engineering Seminar
8.S198: Special Subject: Physics (New)
16.09: Statistics and Probability
9.12: Experimental Molecular Neurobiology
20.S940: Special Subject in Biological Engineering
11.136: Global Mental Health
12.100: Plate Tectonics and Climate (New)
4.191: Independent Study in Architecture Design
4.S00: Special Subject: Design
3.095: Introduction to Metalsmithing
4.130: Architectural Design Theory and Methodologies
7.002: Fundamentals of Experimental Molecular Biology
2.074: Solid Mechanics: Elasticity
24.S20: Special Subject: Philosophy
20.010: Introduction to Experimentation in BE
11.067: Land Use Law and Politics: Race, Place, and Law
3.020: Thermodynamics of Materials
20.201: Fundamentals of Drug Development
18.384: Undergraduate Seminar in Physical Mathematics
24.192: Language, Information, and Power
10.557: Mixed-integer and Nonconvex Optimization
12.203: Mechanics of Earth
4.032: Design Studio: Information Design and Visualization
1.054: Mechanics and Design of Concrete Structures
22.05: Neutron Science and Reactor Physics
6.1600: Foundations of Computer Security
8.16: Data Science in Physics
15.086: Engineering Probability
3.373: Computing Fabrics
10.606: Picturing Science and Engineering
17.271: Mass Incarceration in the United States
20.320: Analysis of Biomolecular and Cellular Systems

Possible reasons for changes in MIT's course catalog:
- Evolving fields and research areas (e.g. new tech)
- Interdisciplinary programs and combined majors  
- Revisions to core curriculum and requirements
- Updated course numbering schemes
- Response to student interest and enrollment trends  
"""

# Observations on discontinued subjects:
# - Span a wide range of departments and topics
# - Include specialized engineering, niche humanities/social science, and graduate seminars
# - May reflect fields that became less relevant or were consolidated/renamed

# Observations on new subjects:
# - Focus on cutting-edge fields like AI/ML, biological engineering, neuroscience
# - Emphasize hands-on projects, design, entrepreneurship 
# - More interdisciplinary topics bridging traditional fields
# - Engage with technology's societal impact and ethics
# - Expanded use of 6-digit course numbers

# Overall trends:
# - Shift toward computing, data science, life sciences, clean energy
# - More project-based and independent study subjects
# - Curriculum changes likely driven by industry needs, research priorities, student interests