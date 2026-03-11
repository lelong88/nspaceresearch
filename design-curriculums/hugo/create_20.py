#!/usr/bin/env python3
"""Create 20 curriculums via curriculum/create API, same structure as Rewriting Extinction."""
import json, requests, time, sys
sys.path.insert(0, "/home/ubuntu/nspaceresearch")
from firebase_token import get_firebase_id_token

API = "https://helloapi.step.is/curriculum/create"
UID = "zs5AMpVfqkcfDf8CJ9qrXdH58d73"

# fmt: off
T = [
  ("The Invisible Architecture of Sleep",
   "Master 10 advanced vocabulary words through an article about sleep neuroscience — circadian rhythms, REM cycles, and glymphatic cleansing.",
   "Every night your brain embarks on an extraordinary journey of repair, memory consolidation, and emotional processing. Learn 10 words through cutting-edge sleep science.",
   ["Circadian","Consolidation","Deprivation","Cognitive","Neurological"],
   ["Insomnia","Melatonin","Restorative","Chronic","Impairment"],
   "The Brain's Nightly Journey", "When Sleep Fails",
   "Every 24 hours, your body follows a circadian rhythm — an internal clock synchronized to the cycle of light and darkness. As night falls, the brain initiates a complex neurological process: consolidation. During deep sleep, the hippocampus replays the day's experiences, transferring fragile short-term memories into durable long-term storage. This cognitive housekeeping is not optional. Even a single night of deprivation — going without adequate sleep — measurably impairs attention, decision-making, and emotional regulation. The brain, it turns out, is never truly resting; it is rebuilding itself, one sleep cycle at a time.",
   "When the circadian system breaks down, the consequences cascade. Chronic insomnia — the persistent inability to fall or stay asleep — affects roughly 10 percent of adults worldwide. Without sufficient restorative sleep, the brain's glymphatic system cannot clear metabolic waste, leading to a buildup of proteins linked to neurodegeneration. Melatonin, the hormone that signals darkness to the body, is often disrupted by blue light from screens. The resulting cognitive impairment extends far beyond grogginess: studies show that chronic sleep loss rivals alcohol intoxication in its effect on reaction time and judgment."),

  ("The Economics of Attention",
   "Master 10 advanced vocabulary words through an article about the attention economy — how tech companies compete for our focus and the movement to reclaim cognitive autonomy.",
   "Your attention is the most valuable commodity of the 21st century. Every notification and infinite scroll is engineered to capture your focus. Learn 10 words through this exploration.",
   ["Commodity","Algorithm","Engagement","Monetize","Surveillance"],
   ["Autonomy","Manipulation","Dopamine","Regulation","Compulsive"],
   "Capturing the Mind", "Reclaiming Your Focus",
   "In the digital age, human attention has become a commodity — something bought, sold, and traded on a global scale. Social media platforms deploy sophisticated algorithms designed to maximize engagement: the longer you scroll, the more advertisements you see, and the more revenue the platform can monetize. Behind every notification ping lies a carefully engineered feedback loop. This is not accidental. It is the product of surveillance capitalism — a system in which your behavioral data is harvested, analyzed, and sold to the highest bidder.",
   "A growing movement is pushing back against the attention economy, demanding greater autonomy over how we spend our cognitive resources. Critics argue that persuasive design techniques amount to manipulation — exploiting the brain's dopamine reward system to create compulsive usage patterns. In the European Union, new regulation requires platforms to offer chronological feeds and disable autoplay by default. Yet the debate remains fierce: can legislation truly protect attention in an era when every app is engineered to be irresistible?"),

  ("Microplastics: The Invisible Invasion",
   "Master 10 advanced vocabulary words through an article about microplastic pollution — how tiny fragments have infiltrated every ecosystem and entered our bloodstreams.",
   "They are in the rain, in the fish on your plate, and in your blood. Microplastics have become the defining pollutant of our era. Learn 10 words through this exploration.",
   ["Pervasive","Contamination","Degradation","Ingestion","Accumulation"],
   ["Toxicity","Filtration","Mitigation","Polymer","Carcinogenic"],
   "A World Saturated in Plastic", "Fighting Back Against Microplastics",
   "Microplastic contamination is now pervasive — present in every ocean, every continent, and even in Arctic ice cores. These tiny fragments result from the degradation of larger plastic items: bottles, bags, and synthetic clothing that slowly break apart under sunlight and mechanical stress. Through ingestion, marine organisms absorb microplastics into their tissues, and the particles move up the food chain through a process called bioaccumulation. Recent studies have detected microplastics in human blood, lung tissue, and placental fluid, raising urgent questions about long-term health effects.",
   "The toxicity of microplastics depends on their polymer composition and the chemical additives they carry. Some plastics leach substances classified as carcinogenic by the World Health Organization. Current water filtration systems capture only a fraction of these particles, and no country has yet implemented comprehensive mitigation strategies. Scientists are exploring biodegradable alternatives and enzymatic recycling, but the sheer accumulation of plastic already in the environment means that even if all plastic production stopped tomorrow, the crisis would persist for centuries."),

  ("The Language of Color",
   "Master 10 advanced vocabulary words through an article about the science and psychology of color — wavelengths, perception, cultural meaning, and how color influences decisions.",
   "Why does red make your heart beat faster? Why do hospitals paint walls blue? Color is a language that shapes emotion and behavior. Learn 10 words through color science.",
   ["Wavelength","Perception","Pigment","Saturation","Spectrum"],
   ["Connotation","Aesthetic","Subliminal","Chromatic","Synesthesia"],
   "The Physics and Biology of Color", "Color, Culture, and the Mind",
   "Color begins as a wavelength of electromagnetic radiation. When light strikes an object, certain wavelengths are absorbed and others reflected; the reflected wavelengths enter the eye and trigger perception. The pigments in a painter's palette work by the same principle — each absorbs specific wavelengths and reflects the rest. The saturation of a color describes its intensity: a vivid red is highly saturated, while a faded pink is desaturated. The visible spectrum — the narrow band of wavelengths the human eye can detect — represents only a tiny fraction of all electromagnetic radiation.",
   "Beyond physics, color carries connotation — cultural and emotional meaning that varies across societies. White symbolizes purity in Western weddings but mourning in parts of East Asia. Designers leverage aesthetic principles to create chromatic harmonies that feel pleasing or unsettling. Much of color's influence is subliminal: studies show that people rate food as tastier when served on certain colored plates, without conscious awareness. In rare cases, individuals experience synesthesia — a neurological condition in which perceiving one sense automatically triggers another, such as seeing colors when hearing music."),

  ("Fermentation: The Ancient Biotechnology",
   "Master 10 advanced vocabulary words through an article about fermentation — the biological process behind bread, beer, cheese, and modern biotechnology.",
   "Long before humans understood chemistry, they harnessed fermentation — the metabolic magic of microbes. Learn 10 words through this exploration of ancient and modern fermentation.",
   ["Fermentation","Microorganism","Metabolism","Catalyst","Substrate"],
   ["Probiotic","Pasteurization","Cultivation","Anaerobic","Symbiotic"],
   "The Science Behind the Bubbles", "Fermentation in the Modern World",
   "Fermentation is one of the oldest biotechnologies on Earth. At its core, it is a metabolic process in which microorganisms — bacteria, yeasts, and molds — break down a substrate such as sugar in the absence of oxygen. These microscopic catalysts convert glucose into ethanol, carbon dioxide, lactic acid, or other byproducts, depending on the species involved. The bubbles in bread dough, the tang of yogurt, and the complexity of aged wine all result from this ancient biochemical transformation.",
   "In the modern era, fermentation has expanded far beyond the kitchen. Probiotic foods — containing live beneficial bacteria — have become a global health trend, supported by growing evidence that gut microbiota influence immunity, mood, and metabolism. Pasteurization, the heat treatment that kills harmful microorganisms, revolutionized food safety but also sparked debate about whether it destroys beneficial cultures. Scientists are now cultivating engineered microbes in anaerobic bioreactors to produce everything from insulin to sustainable aviation fuel. The symbiotic relationship between humans and microbes is not just ancient history — it is the frontier of biotechnology."),

  ("The Psychology of Procrastination",
   "Master 10 advanced vocabulary words through an article about procrastination — why we delay important tasks, the neuroscience behind avoidance, and strategies to overcome it.",
   "You know the deadline is tomorrow. You know you should start now. And yet you open another browser tab. Learn 10 words through the science of procrastination.",
   ["Procrastination","Aversion","Impulse","Gratification","Prefrontal"],
   ["Perfectionism","Paralysis","Accountability","Incremental","Momentum"],
   "Why We Delay", "Breaking the Cycle",
   "Procrastination is not laziness — it is an emotional regulation problem. When we face a task that triggers aversion — anxiety, boredom, or self-doubt — the brain's impulse system hijacks decision-making. The limbic system, which craves immediate gratification, overpowers the prefrontal cortex, the region responsible for long-term planning and self-control. The result is a predictable pattern: we choose short-term comfort over long-term benefit, then experience guilt, which makes the task feel even more aversive, creating a vicious cycle.",
   "Perfectionism is one of the most powerful drivers of procrastination. When the standard is impossibly high, the fear of failure creates paralysis — the inability to begin at all. Research shows that external accountability — telling someone else about your goal — significantly reduces procrastination by adding social consequences to delay. The most effective strategy, however, is incremental action: breaking a large task into tiny, non-threatening steps. Once you complete the first step, momentum builds — each small win generates the motivation to continue, gradually dissolving the aversion that caused the delay."),

  ("Mapping the Ocean Floor",
   "Master 10 advanced vocabulary words through an article about deep-sea exploration — how sonar, autonomous submarines, and satellite altimetry reveal the hidden ocean topography.",
   "We have better maps of Mars than of our own ocean floor. More than 80 percent of the seabed remains unmapped. Learn 10 words through ocean exploration science.",
   ["Topography","Sonar","Autonomous","Submersible","Hydrothermal"],
   ["Cartography","Bathymetry","Tectonic","Expedition","Uncharted"],
   "Into the Abyss", "The Race to Map the Seabed",
   "The topography of the ocean floor is as dramatic as any landscape on land — yet almost entirely hidden from view. Scientists use sonar — sound waves bounced off the seabed — to build detailed maps of underwater terrain. Autonomous underwater vehicles, or AUVs, can dive to depths no human could survive, collecting data for months without surfacing. Near mid-ocean ridges, submersible expeditions have discovered hydrothermal vents — cracks in the seafloor where superheated water, rich in minerals, supports bizarre ecosystems that thrive without sunlight.",
   "Modern ocean cartography combines satellite altimetry, multibeam sonar, and AI-powered data processing to create increasingly detailed bathymetry maps — three-dimensional representations of the seafloor's depth and shape. These maps reveal the scars of tectonic activity: spreading ridges where new crust is born, subduction zones where old crust is recycled into the mantle, and fracture zones that stretch for thousands of kilometers. The Seabed 2030 expedition aims to map the entire ocean floor by the end of the decade, but vast regions remain uncharted — a reminder that the greatest frontier of exploration lies beneath the waves."),

  ("The Science of Forgiveness",
   "Master 10 advanced vocabulary words through an article about the psychology and neuroscience of forgiveness — how letting go of resentment rewires the brain and improves health.",
   "Forgiveness is not weakness — it is one of the most demanding cognitive feats the human brain can perform. Learn 10 words through the science of forgiveness.",
   ["Resentment","Empathy","Transgression","Rumination","Cortisol"],
   ["Reconciliation","Catharsis","Vulnerability","Compassion","Therapeutic"],
   "The Weight of Grudges", "The Healing Power of Letting Go",
   "Holding a grudge is expensive — biologically speaking. When we replay a transgression in our minds, a process psychologists call rumination, the brain activates the same stress circuits as the original offense. Cortisol, the body's primary stress hormone, floods the bloodstream, elevating blood pressure and suppressing immune function. Over time, chronic resentment literally reshapes the brain, strengthening neural pathways associated with anger and weakening those linked to empathy. Forgiveness, neuroscientists have discovered, is not about condoning the offense — it is about releasing the brain from a self-destructive loop.",
   "Forgiveness does not require reconciliation — you can forgive someone without ever speaking to them again. What it does require is vulnerability: the willingness to confront painful emotions rather than suppress them. Psychologists describe the moment of release as catharsis — a profound emotional discharge that reduces physiological stress markers within minutes. Compassion-focused therapy, a therapeutic approach gaining traction in clinical psychology, trains patients to extend the same kindness to themselves that they would offer a friend. Studies show that people who practice forgiveness report lower anxiety, fewer depressive episodes, and stronger immune function."),

  ("Vertical Farms: Growing Up Instead of Out",
   "Master 10 advanced vocabulary words through an article about vertical farming — indoor agriculture using LED lighting, hydroponics, and AI transforming food production.",
   "What if your salad was grown on the 15th floor of a skyscraper? Vertical farming is turning buildings into food factories. Learn 10 words through indoor agriculture science.",
   ["Hydroponics","Photosynthesis","Yield","Sustainability","Irrigation"],
   ["Scalability","Nutrient","Automation","Arable","Resilient"],
   "Farming Without Soil", "Can Vertical Farms Feed the World?",
   "Vertical farming replaces soil with hydroponics — a system in which plant roots grow in nutrient-rich water solutions. LED lights tuned to specific wavelengths optimize photosynthesis, allowing crops to grow 24 hours a day regardless of weather or season. The yield per square meter can be 100 times greater than traditional agriculture, and water usage drops by up to 95 percent because irrigation systems recirculate every drop. For a world facing climate change and shrinking farmland, sustainability is no longer optional — it is the central challenge of feeding 10 billion people by 2050.",
   "The biggest question facing vertical farming is scalability — whether these high-tech facilities can grow beyond leafy greens to produce staple crops at competitive prices. Each plant requires precise nutrient delivery, and automation powered by AI and robotics is essential to keep labor costs manageable. Critics argue that vertical farms consume enormous amounts of electricity and can never replace the vast tracts of arable land that feed the world today. Proponents counter that resilient, climate-proof food production close to urban consumers will become essential as extreme weather events make traditional farming increasingly unpredictable."),

  ("The Hidden World of Fungi",
   "Master 10 advanced vocabulary words through an article about the fungal kingdom — mycorrhizal networks, decomposition, and how fungi may hold the key to sustainable materials.",
   "Beneath your feet lies a hidden internet — a vast network of fungal threads connecting trees and sharing nutrients. Learn 10 words through the extraordinary kingdom of fungi.",
   ["Mycelium","Decomposition","Symbiosis","Spore","Substrate"],
   ["Mycorrhizal","Bioluminescent","Pathogen","Antibiotic","Biodegradable"],
   "The Underground Network", "Fungi as Problem Solvers",
   "Fungi are neither plants nor animals — they belong to their own kingdom, and they are everywhere. The visible mushroom is merely the fruiting body; the true organism is the mycelium, a vast web of microscopic threads that can stretch for kilometers underground. Fungi are nature's master recyclers: through decomposition, they break down dead organic matter and return essential nutrients to the soil. Many fungi form symbiosis with plant roots, exchanging minerals for sugars in a partnership so ancient it predates the evolution of roots themselves. Reproduction happens through spores — microscopic packets of genetic material released by the millions, carried by wind and water to colonize new substrate.",
   "The mycorrhizal network — sometimes called the 'wood wide web' — connects up to 90 percent of land plants, allowing trees to share nutrients and even warn neighbors of insect attacks through chemical signals. Some fungi are bioluminescent, glowing in the dark to attract insects that spread their spores. Others are deadly: fungal pathogens cause devastating crop diseases and life-threatening infections in humans. Yet fungi have also given us some of our most important medicines — penicillin, the first antibiotic, was derived from a common mold. Today, researchers are engineering fungi to produce biodegradable packaging, construction materials, and even leather alternatives."),

  ("The Mathematics of Music",
   "Master 10 advanced vocabulary words through an article about the deep connection between mathematics and music — frequency ratios, harmony, rhythm as pattern, and algorithmic composition.",
   "Pythagoras discovered it 2,500 years ago: music is mathematics made audible. Every chord and melody follows precise mathematical relationships. Learn 10 words through the math of music.",
   ["Frequency","Harmony","Ratio","Resonance","Interval"],
   ["Tempo","Symmetry","Algorithmic","Dissonance","Oscillation"],
   "Numbers in Sound", "When Machines Compose",
   "Every musical note is a vibration at a specific frequency — middle C, for example, vibrates at 261.6 times per second. Harmony arises when two frequencies share a simple mathematical ratio: an octave is a 2:1 ratio, a perfect fifth is 3:2. When these ratios align, the sound waves reinforce each other through resonance, producing a sensation the brain perceives as pleasant. The interval between notes — the distance in pitch — determines whether a chord sounds bright, dark, tense, or resolved. Music, at its deepest level, is the art of organizing mathematical relationships in time.",
   "Rhythm, too, is mathematical: tempo is measured in beats per minute, and rhythmic patterns exhibit symmetry, repetition, and variation — the same structural principles found in fractals and tiling. In 2026, algorithmic composition has moved from novelty to mainstream: AI systems trained on millions of scores can generate original music in any style. Yet human listeners consistently prefer music that balances consonance with moments of dissonance — unexpected tension that resolves into satisfaction. The oscillation between predictability and surprise, mathematicians argue, is what makes music emotionally powerful — and what remains hardest for algorithms to replicate."),

  ("The Paradox of Choice",
   "Master 10 advanced vocabulary words through an article about decision-making psychology — why more options often lead to worse decisions and less satisfaction.",
   "A supermarket offers 30 types of jam. A streaming service offers 10,000 movies. Yet instead of feeling liberated, you feel paralyzed. Learn 10 words through the paradox of choice.",
   ["Paradox","Abundance","Deliberation","Cognitive","Overwhelm"],
   ["Satisficing","Maximizer","Regret","Heuristic","Threshold"],
   "Too Many Options", "Deciding How to Decide",
   "The paradox of choice describes a counterintuitive phenomenon: as the number of options increases, satisfaction decreases. In an era of abundance — unlimited products, careers, and lifestyles to choose from — the process of deliberation becomes exhausting. Every decision demands cognitive resources: comparing features, imagining outcomes, weighing trade-offs. When the options are too many, the brain experiences overwhelm — a state of mental fatigue that leads to either impulsive decisions or no decision at all.",
   "Psychologists distinguish between two decision-making styles. Satisficers choose the first option that meets a minimum threshold of acceptability — 'good enough' is good enough. Maximizers, by contrast, exhaustively compare every option, seeking the absolute best. Research consistently shows that maximizers experience more regret, more anxiety, and less happiness with their choices. The solution, behavioral scientists suggest, is to adopt heuristics — simple mental shortcuts that reduce the cognitive burden of decision-making. Setting a threshold in advance and accepting that 'good enough' is often optimal can transform choosing from stress into freedom."),

  ("Biomimicry: Nature's Design Playbook",
   "Master 10 advanced vocabulary words through an article about biomimicry — how engineers copy nature's solutions, from bullet trains inspired by kingfishers to adhesives modeled on gecko feet.",
   "The kingfisher's beak inspired the bullet train. The lotus leaf inspired self-cleaning paint. Learn 10 words through the science of stealing nature's best ideas.",
   ["Biomimicry","Adaptation","Aerodynamic","Structural","Innovation"],
   ["Prototype","Adhesion","Turbulence","Replication","Sustainable"],
   "Learning from 3.8 Billion Years of R&D", "From Nature to Engineering",
   "Biomimicry is the practice of studying nature's designs and processes, then applying them to solve human engineering challenges. Evolution has been running experiments for 3.8 billion years, and the organisms that survive represent optimized solutions to problems of structural strength, energy efficiency, and adaptation to harsh environments. The kingfisher's aerodynamic beak, for example, inspired the nose cone of Japan's Shinkansen bullet train, reducing noise and energy consumption by 15 percent. Every innovation in biomimicry begins with a simple question: how has nature already solved this problem?",
   "Translating biological designs into engineering prototypes is rarely straightforward. Gecko feet achieve extraordinary adhesion through millions of microscopic hair-like structures that exploit van der Waals forces — but replicating this at industrial scale remains a challenge. The tubercles on humpback whale fins reduce turbulence and improve lift, inspiring more efficient wind turbine blades. The key insight of biomimicry is that nature's solutions are inherently sustainable — they use minimal energy, produce no toxic waste, and are fully biodegradable. As engineers face mounting pressure to design for a circular economy, the replication of nature's strategies is shifting from curiosity to necessity."),

  ("The Art of Negotiation",
   "Master 10 advanced vocabulary words through an article about negotiation — the psychology, strategy, and communication skills that determine whether deals succeed or fail.",
   "Every day, you negotiate — with colleagues, with family, with yourself. Yet most people approach negotiation with instinct rather than strategy. Learn 10 words through negotiation science.",
   ["Leverage","Concession","Stakeholder","Proposition","Impasse"],
   ["Reciprocity","Anchoring","Mediation","Compromise","Assertive"],
   "The Mechanics of the Deal", "Psychology at the Bargaining Table",
   "Negotiation is the process of reaching agreement between parties with different interests. The foundation of any negotiation is leverage — the power one side holds over the other, whether through information, alternatives, or time pressure. Skilled negotiators prepare by identifying every stakeholder involved, crafting a clear proposition, and determining in advance what concessions they are willing to make. The goal is not to 'win' but to find a solution both sides can accept. When neither party will budge, the negotiation reaches an impasse — a deadlock that requires creative problem-solving to break.",
   "The psychology of negotiation is as important as the strategy. Reciprocity — the human tendency to return favors — means that making a small concession often triggers a larger one from the other side. Anchoring, the cognitive bias in which the first number mentioned disproportionately influences the final outcome, gives a powerful advantage to whoever speaks first. When direct negotiation fails, mediation — the involvement of a neutral third party — can help both sides find compromise without losing face. The most effective negotiators are assertive without being aggressive: they state their needs clearly, listen actively, and search for solutions that expand the pie rather than simply dividing it."),

  ("Quantum Computing: Beyond the Binary",
   "Master 10 advanced vocabulary words through an article about quantum computing — how qubits, superposition, and entanglement could revolutionize cryptography, drug discovery, and AI.",
   "Classical computers think in ones and zeros. Quantum computers think in possibilities. Learn 10 words through the technology that could solve problems no classical computer ever will.",
   ["Qubit","Superposition","Entanglement","Exponential","Encryption"],
   ["Decoherence","Simulation","Optimization","Scalable","Theoretical"],
   "The Quantum Leap", "Promise, Peril, and Progress",
   "A classical computer stores information as bits — each either 0 or 1. A quantum computer uses qubits, which exploit a property called superposition to exist as 0, 1, or both simultaneously. When qubits become entangled — linked so that the state of one instantly influences the other regardless of distance — their combined processing power grows exponentially. A quantum computer with just 300 fully stable qubits could perform more calculations simultaneously than there are atoms in the observable universe. This power threatens current encryption systems, which rely on the difficulty of factoring large numbers.",
   "The greatest obstacle to practical quantum computing is decoherence — the tendency of qubits to lose their quantum properties when they interact with the environment. Maintaining qubit stability requires temperatures near absolute zero and extraordinary isolation. Despite these challenges, quantum simulation of molecular behavior is already accelerating drug discovery, and quantum optimization algorithms are improving logistics and financial modeling. Whether quantum computing can become truly scalable — reliable enough for general-purpose use — remains an open question. What was once purely theoretical is now a multibillion-dollar engineering race."),

  ("The Sociology of Loneliness",
   "Master 10 advanced vocabulary words through an article about the loneliness epidemic — how social isolation affects the brain and body, and what communities are doing to fight back.",
   "We are more connected than ever — and lonelier than ever. Loneliness is now classified as a public health crisis. Learn 10 words through the science of loneliness.",
   ["Isolation","Epidemic","Mortality","Physiological","Cortisol"],
   ["Belonging","Stigma","Intervention","Communal","Resilience"],
   "The Biology of Being Alone", "Rebuilding Connection",
   "Loneliness is not the same as being alone — it is the painful perception that your social connections are inadequate. This subjective isolation triggers a cascade of physiological responses: cortisol levels rise, inflammation increases, and the immune system weakens. Chronic loneliness has been linked to a 26 percent increase in mortality risk, placing it alongside obesity and smoking as a leading public health threat. The epidemic is global: surveys found that one in four adults worldwide reported feeling lonely most or all of the time.",
   "Addressing loneliness requires more than telling people to 'get out more.' The stigma surrounding loneliness — the shame of admitting you feel disconnected — prevents many from seeking help. Effective intervention programs focus on building a sense of belonging through structured communal activities: shared meals, volunteer projects, intergenerational mentoring. Researchers emphasize that resilience against loneliness is not about the quantity of social contacts but the quality — a single deep, trusting relationship can be more protective than a hundred superficial ones."),

  ("The Ethics of Artificial Intelligence",
   "Master 10 advanced vocabulary words through an article about AI ethics — how bias enters algorithms, why transparency matters, and the global debate over regulating AI.",
   "An algorithm denies your loan. Another decides your prison sentence. As AI makes increasingly consequential decisions, ethics has never been more urgent. Learn 10 words through AI ethics.",
   ["Bias","Transparency","Accountability","Autonomous","Discriminatory"],
   ["Governance","Surveillance","Consent","Equitable","Precedent"],
   "When Machines Judge", "Governing the Ungovernable",
   "Artificial intelligence systems are making decisions that profoundly affect human lives — hiring, lending, sentencing, diagnosing — yet most operate as black boxes, offering no transparency into how conclusions are reached. The problem begins with bias: AI models learn from historical data, and if that data reflects discriminatory patterns, the algorithm reproduces and amplifies those patterns at scale. The question of accountability is equally thorny: when an autonomous vehicle causes an accident or a medical AI misdiagnoses a patient, who is responsible?",
   "The global debate over AI governance is intensifying. The European Union's AI Act classifies AI systems by risk level and bans those deemed unacceptably dangerous, such as real-time biometric surveillance in public spaces. Central to the debate is consent — whether individuals have the right to know when AI is making decisions about them. Courts are setting new legal precedent with every ruling, but the technology evolves faster than the law. Building equitable AI requires not just better algorithms but diverse teams, inclusive datasets, and a commitment to designing systems that serve all of humanity."),

  ("The Science of Habit Formation",
   "Master 10 advanced vocabulary words through an article about how habits form in the brain — the cue-routine-reward loop and evidence-based strategies for building good habits.",
   "You do it without thinking — reaching for your phone, biting your nails, brewing coffee the moment you wake up. Learn 10 words through the science of habit formation.",
   ["Habitual","Cue","Reinforcement","Neuroplasticity","Automaticity"],
   ["Willpower","Relapse","Substitution","Incremental","Sustainable"],
   "How Habits Wire the Brain", "Rewiring Your Routines",
   "A habit is a behavior that has become so deeply encoded in the brain that it requires almost no conscious thought — a state neuroscientists call automaticity. The process begins with a cue: a time, place, emotion, or preceding action that triggers the behavior. The behavior itself is the routine, and the reward that follows provides reinforcement, strengthening the neural pathway. Over time, through neuroplasticity — the brain's ability to reorganize itself — the basal ganglia takes over, running the habitual loop on autopilot while the prefrontal cortex is freed for other tasks.",
   "Breaking a bad habit is notoriously difficult because the neural pathway never fully disappears — it can always be reactivated. Willpower alone is unreliable; studies show it depletes like a battery over the course of the day. The most effective strategy is substitution: keeping the same cue and reward but replacing the routine with a healthier behavior. Change must be incremental — attempting to overhaul multiple habits simultaneously almost guarantees relapse, the return to old patterns. Sustainable habit change requires patience, self-compassion, and environmental design: removing cues for unwanted habits and making desired behaviors as effortless as possible."),

  ("The Architecture of Bridges",
   "Master 10 advanced vocabulary words through an article about bridge engineering — how suspension, arch, and cable-stayed designs distribute forces and push the limits of what bridges can span.",
   "A bridge is a conversation between gravity and geometry. Every cable, every arch, every beam is a calculated answer to the pull of the Earth. Learn 10 words through bridge engineering.",
   ["Suspension","Compression","Tension","Span","Foundation"],
   ["Cantilever","Aerodynamic","Corrosion","Reinforced","Magnitude"],
   "Forces in Balance", "Engineering the Impossible",
   "Every bridge must solve the same fundamental problem: how to support its own weight and the weight of traffic across an open span while resisting gravity, wind, and vibration. The two primary forces at work are compression — the pushing force that shortens materials — and tension — the pulling force that stretches them. Arch bridges channel loads into compression, directing force downward and outward into the foundation. Suspension bridges hang the roadway from massive cables under tension, transferring the load to towers and anchorages at each end.",
   "Modern bridge engineering pushes the boundaries of physics and materials science. Cantilever bridges extend outward from supports without external bracing, relying on precise balance and reinforced concrete or steel. The aerodynamic shaping of bridge decks prevents wind-induced oscillation — lessons learned from the catastrophic collapse of the Tacoma Narrows Bridge in 1940. Corrosion, the gradual chemical destruction of metal by moisture and salt, remains the greatest long-term threat to steel bridges. The magnitude of modern bridge projects is staggering: China's Danyang-Kunshan Grand Bridge stretches 164 kilometers."),

  ("The Psychology of Crowds",
   "Master 10 advanced vocabulary words through an article about crowd psychology — how individuals behave differently in groups, mob mentality, and how understanding crowds prevents disasters.",
   "Put a hundred calm, rational individuals together and something strange happens — they become a crowd, and crowds follow rules of their own. Learn 10 words through crowd psychology.",
   ["Conformity","Anonymity","Contagion","Deindividuation","Threshold"],
   ["Stampede","Dispersal","Surveillance","Catalyst","Polarization"],
   "The Mind of the Mob", "Managing the Masses",
   "In a crowd, individual identity dissolves. Psychologists call this deindividuation — the loss of self-awareness and personal responsibility that occurs when people feel anonymous within a group. Conformity pressures intensify: individuals adopt the behavior of those around them, even when it contradicts their private beliefs. Emotional contagion spreads through crowds like a virus — fear, excitement, and anger leap from person to person. Sociologist Mark Granovetter's threshold model explains why riots erupt: each person has a different threshold of how many others must act before they join in.",
   "Understanding crowd dynamics is essential for preventing disasters. A stampede — a sudden, uncontrolled surge of people — kills hundreds every year at religious gatherings, concerts, and sporting events. Modern crowd management uses surveillance cameras and AI-powered density analysis to detect dangerous compression before it becomes lethal, triggering early dispersal strategies. Yet crowds are not always destructive. A single catalyst — a speech, a shared experience — can unite thousands in peaceful solidarity. The challenge is understanding when group polarization tips from productive energy into dangerous action."),

  ("The Future of Money",
   "Master 10 advanced vocabulary words through an article about the evolution of money — from gold to digital currencies, central bank digital currencies, and the cashless society debate.",
   "Money is a shared fiction — a story we all agree to believe. But the story is changing faster than ever. Learn 10 words through the past, present, and future of money.",
   ["Currency","Inflation","Decentralized","Ledger","Volatility"],
   ["Sovereignty","Liquidity","Speculation","Interoperability","Deflationary"],
   "From Gold to Code", "The Cashless Frontier",
   "For most of human history, currency took physical form — shells, coins, banknotes — objects whose value was backed by scarcity or government decree. The invention of the decentralized digital ledger, or blockchain, challenged this model by enabling peer-to-peer transactions without a central authority. Bitcoin demonstrated that trust could be maintained through mathematics rather than institutions. Yet the volatility of cryptocurrencies — wild price swings driven by speculation — has prevented them from functioning as stable mediums of exchange. Meanwhile, inflation — the gradual erosion of purchasing power — continues to shape the monetary policies of every nation.",
   "Central banks are now developing their own digital currencies (CBDCs), seeking to combine the efficiency of digital payments with the sovereignty and stability of government-backed money. The key technical challenge is interoperability — ensuring that different digital currency systems can communicate seamlessly across borders. Critics warn that CBDCs could enable unprecedented financial surveillance, while proponents argue they could bring banking services to the 1.4 billion adults worldwide who remain unbanked. Some economists predict a deflationary future in which programmable money automatically adjusts its supply. The debate over liquidity, control, and freedom is far from settled."),
]
# fmt: on


def mk_items(vocab, topic):
    return [{"prompt": f"Use '{w.lower()}' in a sentence about {topic.lower()}.", "targetVocab": w.lower()} for w in vocab]

def mk_session(n, title, vocab, reading, all_vocab, topic_title):
    short = title
    acts = [
        {"title": f"Session {n} Introduction & Vocabulary",
         "description": f"Learn vocabulary for Session {n}: {', '.join(v.lower() for v in vocab)}",
         "activityType": "introAudio", "practiceMinutes": 6,
         "data": {"text": f"In this session you'll learn: {', '.join(vocab)}.", "audioSpeed": 0.01}},
        {"title": f"Flashcards: {short}", "description": f"Study: {', '.join(vocab)}",
         "activityType": "viewFlashcards", "practiceMinutes": 4,
         "data": {"vocabList": vocab, "audioSpeed": 0.01}},
        {"title": f"Speak Flashcards: {short}", "description": f"Practice saying: {', '.join(vocab)}",
         "activityType": "speakFlashcards", "practiceMinutes": 3,
         "data": {"vocabList": vocab, "audioSpeed": 0.01}},
        {"title": f"Recognition Drill: {short}", "description": "Choose the correct definition",
         "activityType": "vocabLevel1", "practiceMinutes": 5,
         "data": {"vocabList": vocab, "audioSpeed": 0.01}},
        {"title": f"Active Recall: {short}", "description": "Supply the correct word without hints",
         "activityType": "vocabLevel2", "practiceMinutes": 5,
         "data": {"vocabList": vocab, "audioSpeed": 0.01}},
        {"title": f"Understand: {short}", "description": "Demonstrate understanding in context",
         "activityType": "vocabLevel3", "practiceMinutes": 5,
         "data": {"vocabList": vocab, "audioSpeed": 0.01}},
        {"title": f"Short Reading: {short}", "description": f"Read a passage with Session {n} vocabulary",
         "activityType": "reading", "practiceMinutes": 5,
         "data": {"text": reading, "audioSpeed": 0.01}},
        {"title": f"Speak Along: {short}", "description": "Practice speaking the passage aloud",
         "activityType": "speakReading", "practiceMinutes": 5,
         "data": {"text": reading, "audioSpeed": 0.01}},
        {"title": f"Listen: {short}", "description": f"Listen to the Session {n} passage",
         "activityType": "readAlong", "practiceMinutes": 2,
         "data": {"text": reading, "audioSpeed": 0.01}},
        {"title": "Write Sentences with Target Vocabulary",
         "description": f"Write sentences using: {', '.join(vocab)}",
         "activityType": "writingSentence", "practiceMinutes": 8,
         "data": {"vocabList": vocab, "audioSpeed": 0.01, "items": mk_items(vocab, topic_title)}},
        {"title": "Write a Short Paragraph",
         "description": f"Write 4-6 sentences using at least 3 of 5 vocabulary words",
         "activityType": "writingParagraph", "practiceMinutes": 10,
         "data": {"vocabList": vocab, "audioSpeed": 0.01,
                  "instructions": "Write 4-6 sentences. Use at least 3 out of 5 vocabulary words.",
                  "prompts": [f"Explain a key concept from {topic_title.lower()} using Session {n} vocabulary.",
                              f"Share your thoughts on {topic_title.lower()} using at least 3 vocabulary words."],
                  "rubric": ["Uses at least 3 of 5 vocabulary words", "Vocabulary used in context",
                             "Clear grammar", "Clear main idea and coherence"]}},
    ]
    return {"title": f"Session {n}: {title}", "activities": acts}

def mk_review(all_vocab, topic_title):
    return {"title": "Session 3: Full Vocabulary Review", "activities": [
        {"title": "Review Introduction", "description": "Review guidance for all 10 words",
         "activityType": "introAudio", "practiceMinutes": 1,
         "data": {"text": f"Review all 10 words before the full article in Session 4!", "audioSpeed": 0.01}},
        {"title": "Review All Vocabulary", "description": "Flashcards for all 10 words",
         "activityType": "viewFlashcards", "practiceMinutes": 6,
         "data": {"vocabList": all_vocab, "audioSpeed": 0.01}},
        {"title": "Quick Check: Recognition", "description": "Multiple choice for all 10 words",
         "activityType": "vocabLevel1", "practiceMinutes": 10,
         "data": {"vocabList": all_vocab, "audioSpeed": 0.01}},
        {"title": "Deep Check: Active Recall", "description": "Supply the correct word from memory",
         "activityType": "vocabLevel2", "practiceMinutes": 10,
         "data": {"vocabList": all_vocab, "audioSpeed": 0.01}},
        {"title": "Understand: All Vocabulary", "description": "Demonstrate understanding of all 10 words",
         "activityType": "vocabLevel3", "practiceMinutes": 10,
         "data": {"vocabList": all_vocab, "audioSpeed": 0.01}},
        {"title": "Write a Comprehensive Paragraph",
         "description": "Write 5-7 sentences using at least 6 of 10 vocabulary words",
         "activityType": "writingParagraph", "practiceMinutes": 12,
         "data": {"vocabList": all_vocab, "audioSpeed": 0.01,
                  "instructions": "Write 5-7 sentences. Use at least 6 out of 10 vocabulary words from both sessions.",
                  "prompts": [f"Explain the key ideas from {topic_title.lower()} in your own words.",
                              f"If explaining {topic_title.lower()} to a friend, what would you say?"],
                  "rubric": ["Uses at least 6 of 10 words", "Words from both sessions",
                             "Clear grammar", "Clear main idea", "Shows understanding"]}},
    ]}

def mk_final(all_vocab, topic_title, full_article):
    return {"title": "Session 4: Read the Full Article", "activities": [
        {"title": "Final Reading Introduction", "description": "Guidance before the complete article",
         "activityType": "introAudio", "practiceMinutes": 1,
         "data": {"text": f"Read the complete article about {topic_title.lower()}. Notice how each word fits naturally.", "audioSpeed": 0.01}},
        {"title": f"Full Article: {topic_title}", "description": "Read the complete article",
         "activityType": "reading", "practiceMinutes": 15,
         "data": {"text": full_article, "audioSpeed": 0.01}},
        {"title": "Speak Along: Full Article", "description": "Practice speaking the complete article",
         "activityType": "speakReading", "practiceMinutes": 15,
         "data": {"text": full_article, "audioSpeed": 0.01}},
        {"title": "Listen: Full Article", "description": "Listen to the complete article",
         "activityType": "readAlong", "practiceMinutes": 3,
         "data": {"text": full_article, "audioSpeed": 0.01}},
        {"title": "Advanced Comprehensive Writing",
         "description": "Write 6-8 sentences using at least 8 of 10 vocabulary words",
         "activityType": "writingParagraph", "practiceMinutes": 15,
         "data": {"vocabList": all_vocab, "audioSpeed": 0.01,
                  "instructions": "Write 6-8 sentences. Use at least 8 out of 10 vocabulary words. Show deep analysis.",
                  "prompts": [f"Write a letter explaining what you learned about {topic_title.lower()}.",
                              f"As a journalist, summarize {topic_title.lower()} and why it matters."],
                  "rubric": ["Uses at least 8 of 10 words", "Words from both sessions",
                             "Deep understanding", "Connected ideas", "Varied sentence structure", "Logical flow"]}},
        {"title": "Vocabulary Overview & Congratulations", "description": "Summary and farewell",
         "activityType": "introAudio", "practiceMinutes": 4,
         "data": {"text": f"Congratulations on completing '{topic_title}'! You mastered: {', '.join(all_vocab)}. Well done!", "audioSpeed": 0.01}},
    ]}

def build(t):
    title, desc, preview, v1, v2, s1t, s2t, r1, r2 = t
    full = r1 + "\n\n" + r2
    av = v1 + v2
    return {"title": title, "preview": {"text": preview}, "description": desc,
            "learningSessions": [mk_session(1, s1t, v1, r1, av, title),
                                 mk_session(2, s2t, v2, r2, av, title),
                                 mk_review(av, title), mk_final(av, title, full)]}

def upload(content):
    token = get_firebase_id_token(UID)
    r = requests.post(API, json={"uid": UID, "language": "en", "userLanguage": "en", "content": json.dumps(content), "firebaseIdToken": token})
    r.raise_for_status()
    return r.json()

def main():
    topics = T[:20]  # Limit to 20
    print(f"Creating {len(topics)} curriculums...\n")
    ok = 0
    for i, t in enumerate(topics):
        print(f"[{i+1}/{len(T)}] {t[0]}...", end=" ", flush=True)
        try:
            res = upload(build(t))
            print(f"✓ ID: {res.get('id','?')}")
            ok += 1
        except Exception as e:
            print(f"✗ {e}")
        time.sleep(1)
    print(f"\nDone: {ok}/{len(topics)} created successfully.")

if __name__ == "__main__":
    main()
