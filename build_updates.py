import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove Tilt
html = re.sub(r'<!-- Vanilla Tilt for 3D Cards -->.*?</script>\s*</body>', '</body>', html, flags=re.DOTALL)

# 2. Dark Mode Toggle & CSS Variables
nav_target = """<nav class="navbar liquid-glass" id="navbar">
        <div class="nav-indicator" id="navIndicator"></div>"""
nav_replacement = """<nav class="navbar liquid-glass" id="navbar">
        <div class="nav-indicator" id="navIndicator"></div>
        <button id="themeToggle" class="theme-toggle" aria-label="Toggle Dark Mode">
            <svg class="sun-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line></svg>
            <svg class="moon-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg>
        </button>"""
html = html.replace(nav_target, nav_replacement)

css_append = """
        /* ===== THEME TOGGLE & DARK MODE ===== */
        :root[data-theme="dark"] {
            --bg-color: #0f172a;
            --text-primary: #f8fafc;
            --text-secondary: #cbd5e1;
            --glass-bg: rgba(15, 23, 42, 0.6);
            --glass-border-top: rgba(255, 255, 255, 0.1);
            --glass-border-bottom: rgba(255, 255, 255, 0.05);
            --glass-shadow: 0 8px 32px rgba(0, 0, 0, 0.5);
            --glass-highlight: rgba(255, 255, 255, 0.05);
        }
        .theme-toggle {
            background: rgba(255, 255, 255, 0.1);
            border: 1px solid var(--glass-border-top);
            border-radius: 50%;
            width: 40px;
            height: 40px;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            color: var(--text-primary);
            backdrop-filter: blur(10px);
            transition: var(--transition-smooth);
            margin-left: auto;
            margin-right: 16px;
        }
        .theme-toggle:hover {
            transform: scale(1.1);
            background: rgba(255, 255, 255, 0.2);
        }
        .sun-icon, .moon-icon { width: 20px; height: 20px; }
        :root[data-theme="dark"] .moon-icon { display: none; }
        :root:not([data-theme="dark"]) .sun-icon { display: none; }
        
        body { transition: background-color 0.5s ease, color 0.5s ease; }
        
        /* ===== EXPERIENCE SECTION ===== */
        .timeline {
            position: relative;
            max-width: 800px;
            margin: 0 auto;
            padding: 40px 0;
        }
        .timeline::after {
            content: '';
            position: absolute;
            width: 2px;
            background: var(--text-tertiary);
            top: 0;
            bottom: 0;
            left: 50%;
            margin-left: -1px;
            opacity: 0.3;
        }
        .timeline-item {
            padding: 10px 40px;
            position: relative;
            background: inherit;
            width: 50%;
            box-sizing: border-box;
        }
        .timeline-item::after {
            content: '';
            position: absolute;
            width: 16px;
            height: 16px;
            right: -8px;
            background: var(--bg-color);
            border: 4px solid #24A1DE;
            top: 15px;
            border-radius: 50%;
            z-index: 1;
        }
        .left { left: 0; text-align: right; }
        .right { left: 50%; }
        .right::after { left: -8px; }
        .timeline-content {
            padding: 24px;
            border-radius: var(--radius-md);
            position: relative;
            text-align: left;
        }
        .timeline-date { color: #24A1DE; font-weight: 600; font-size: 0.9em; margin-bottom: 8px; }
        .timeline-title { font-size: 1.2em; font-weight: 700; margin-bottom: 8px; color: var(--text-primary); }
        .timeline-desc { color: var(--text-secondary); font-size: 0.95em; line-height: 1.5; }
        @media (max-width: 768px) {
            .timeline::after { left: 31px; }
            .timeline-item { width: 100%; padding-left: 70px; padding-right: 25px; text-align: left; }
            .timeline-item::after { left: 23px; }
            .right { left: 0%; }
            .left::after { right: auto; }
        }

        /* ===== GITHUB STATS ===== */
        .github-stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 24px;
            margin-top: 40px;
        }
        .stat-card {
            text-align: center;
            padding: 32px 24px;
            display: flex;
            flex-direction: column;
            gap: 12px;
        }
        .stat-icon {
            margin: 0 auto;
            color: var(--text-primary);
        }
        .stat-number {
            font-size: 2.5em;
            font-weight: 800;
            color: #24A1DE;
            font-family: 'Bebas Neue', sans-serif;
            letter-spacing: 1px;
        }
        .stat-label {
            font-size: 0.9em;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 1px;
            color: var(--text-secondary);
        }
        .github-profile-btn {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            margin-top: 32px;
            padding: 12px 24px;
            background: rgba(255, 255, 255, 0.1);
            border: 1px solid var(--glass-border-top);
            border-radius: var(--radius-xl);
            color: var(--text-primary);
            text-decoration: none;
            font-weight: 600;
            transition: var(--transition-smooth);
        }
        .github-profile-btn:hover {
            background: #24A1DE;
            color: #fff;
            transform: translateY(-2px);
        }
        </style>"""
html = html.replace('</style>', css_append)

# 3. Download CV Button in Hero section
hero_actions_target = """<div class="hero-actions reveal delay-3">
                <a href="#contact" class="btn btn-primary">
                    Contact Me
                </a>
                <a href="#projects" class="btn btn-secondary liquid-glass">
                    View Projects
                </a>
            </div>"""
hero_actions_replacement = """<div class="hero-actions reveal delay-3" style="display: flex; gap: 16px; flex-wrap: wrap; justify-content: center;">
                <a href="https://drive.google.com/file/d/1UO5uxQmP2qz2CGk-2u9LzAhnsrsMG15n/view?usp=sharing" target="_blank" class="btn btn-primary" style="display: flex; align-items: center; gap: 8px; background: #24A1DE; color: white; text-decoration: none; border: none; outline: none; border-radius: var(--radius-xl); padding: 16px 32px; font-weight: 600; transition: var(--transition-smooth);">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
                    Download CV
                </a>
                <a href="#contact" class="btn btn-secondary liquid-glass">
                    Contact Me
                </a>
                <a href="#projects" class="btn btn-secondary liquid-glass">
                    View Projects
                </a>
            </div>"""
html = html.replace(hero_actions_target, hero_actions_replacement)

# 4. Experience Section
about_end_target = """</section>

    <!-- PROJECTS -->"""
experience_html = """</section>

    <!-- EXPERIENCE -->
    <section class="section" id="experience">
        <div class="container">
            <div class="section-header reveal">
                <p class="section-label">My Journey</p>
                <h2 class="section-title">Experience</h2>
            </div>
            <div class="timeline">
                <div class="timeline-item left reveal delay-1">
                    <div class="timeline-content glass-card liquid-glass">
                        <div class="timeline-date">2025 - Present</div>
                        <h3 class="timeline-title">Personal Web Developer</h3>
                        <p class="timeline-desc">Building personal and educational web projects using HTML, CSS, and JavaScript.</p>
                    </div>
                </div>
                <div class="timeline-item right reveal delay-2">
                    <div class="timeline-content glass-card liquid-glass">
                        <div class="timeline-date">2025 - Present</div>
                        <h3 class="timeline-title">Telegram Bot Developer</h3>
                        <p class="timeline-desc">Creating Telegram bots for automation and productivity.</p>
                    </div>
                </div>
                <div class="timeline-item left reveal delay-3">
                    <div class="timeline-content glass-card liquid-glass">
                        <div class="timeline-date">2024 - Present</div>
                        <h3 class="timeline-title">Independent Learner</h3>
                        <p class="timeline-desc">Continuously learning programming, finance, and technology through online courses and self-study.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- PROJECTS -->"""
html = html.replace(about_end_target, experience_html)

# 5. GitHub Statistics Section
projects_end_target = """</section>

    <!-- CERTIFICATES -->"""
github_html = """</section>

    <!-- GITHUB STATS -->
    <section class="section" id="github-stats">
        <div class="container" style="text-align: center;">
            <div class="section-header reveal">
                <p class="section-label">Open Source</p>
                <h2 class="section-title">GitHub Stats</h2>
            </div>
            
            <div class="github-stats-grid reveal delay-1" id="github-stats-container">
                <!-- Stats will be injected here via JS -->
                <p style="color: var(--text-tertiary);">Loading statistics...</p>
            </div>
            
            <a href="https://github.com/s1qosimovv" target="_blank" class="github-profile-btn reveal delay-2">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path></svg>
                View GitHub Profile
            </a>
        </div>
    </section>

    <!-- CERTIFICATES -->"""
html = html.replace(projects_end_target, github_html)

# 6. Add JS
js_append = """
        /* ===== THEME TOGGLE ===== */
        const themeToggle = document.getElementById('themeToggle');
        const root = document.documentElement;
        
        const savedTheme = localStorage.getItem('theme');
        if (savedTheme) {
            root.setAttribute('data-theme', savedTheme);
        }

        if(themeToggle) {
            themeToggle.addEventListener('click', () => {
                if (root.getAttribute('data-theme') === 'dark') {
                    root.removeAttribute('data-theme');
                    localStorage.setItem('theme', 'light');
                } else {
                    root.setAttribute('data-theme', 'dark');
                    localStorage.setItem('theme', 'dark');
                }
            });
        }

        /* ===== GITHUB STATS API ===== */
        async function fetchGitHubStats() {
            const container = document.getElementById('github-stats-container');
            if(!container) return;
            
            try {
                const response = await fetch('https://api.github.com/users/s1qosimovv');
                if (!response.ok) throw new Error('Network response was not ok');
                const data = await response.json();
                
                container.innerHTML = `
                    <div class="stat-card glass-card liquid-glass">
                        <svg class="stat-icon" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg>
                        <span class="stat-number" data-target="${data.public_repos}">0</span>
                        <span class="stat-label">Repositories</span>
                    </div>
                    <div class="stat-card glass-card liquid-glass">
                        <svg class="stat-icon" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>
                        <span class="stat-number" data-target="${data.followers}">0</span>
                        <span class="stat-label">Followers</span>
                    </div>
                    <div class="stat-card glass-card liquid-glass">
                        <svg class="stat-icon" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="8.5" cy="7" r="4"></circle><line x1="20" y1="8" x2="20" y2="14"></line><line x1="23" y1="11" x2="17" y2="11"></line></svg>
                        <span class="stat-number" data-target="${data.following}">0</span>
                        <span class="stat-label">Following</span>
                    </div>
                `;
                
                const counters = container.querySelectorAll('.stat-number');
                counters.forEach(counter => {
                    const target = +counter.getAttribute('data-target');
                    const duration = 2000;
                    const increment = target / (duration / 16);
                    let current = 0;
                    
                    const updateCounter = () => {
                        current += increment;
                        if (current < target) {
                            counter.innerText = Math.ceil(current);
                            requestAnimationFrame(updateCounter);
                        } else {
                            counter.innerText = target;
                        }
                    };
                    updateCounter();
                });
                
            } catch (error) {
                container.innerHTML = `<p style="color: #ff4a4a;">Failed to load GitHub statistics.</p>`;
                console.error('GitHub API error:', error);
            }
        }
        
        let statsFetched = false;
        window.addEventListener('scroll', () => {
            const statsSection = document.getElementById('github-stats');
            if (statsSection && !statsFetched) {
                const rect = statsSection.getBoundingClientRect();
                if (rect.top < window.innerHeight) {
                    fetchGitHubStats();
                    statsFetched = true;
                }
            }
        }, { passive: true });
        
    </script>"""
html = html.replace('</script>', js_append)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Finished building updates!")
