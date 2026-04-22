"""Build all UI pages for GoDirect247 platform."""
import os

HEAD = lambda title, depth: f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://unpkg.com/@phosphor-icons/web@2.1.1/src/regular/style.css">
  <link rel="stylesheet" href="https://unpkg.com/@phosphor-icons/web@2.1.1/src/bold/style.css">
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config={{theme:{{extend:{{colors:{{dark:'#191c1f',gold:'#f3cc20','gold-dark':'#c9a800',brand:'#0682B4',surface:'#f4f4f4',teal:'#00a87e',danger:'#e23b4a',muted:'#8d969e',slate:'#505a63'}},fontFamily:{{display:['Plus Jakarta Sans','sans-serif']}}}}}}}}
  </script>
  <style>
    *{{-webkit-font-smoothing:antialiased}}
    body{{font-family:'Inter',sans-serif}}
    .font-display{{font-family:'Plus Jakarta Sans',sans-serif}}
    @keyframes fadeUp{{from{{opacity:0;transform:translateY(20px)}}to{{opacity:1;transform:translateY(0)}}}}
    .ani1{{animation:fadeUp .6s ease 0s both}}.ani2{{animation:fadeUp .6s ease .1s both}}
    .ani3{{animation:fadeUp .6s ease .2s both}}.ani4{{animation:fadeUp .6s ease .3s both}}
    .ani5{{animation:fadeUp .6s ease .45s both}}
    input,select,textarea{{outline:none}}
    input:focus,select:focus,textarea:focus{{box-shadow:0 0 0 2px #f3cc20}}
  </style>
</head>"""

# ─────────────────────────────────────────────────────────────────────────────
# LANDING PAGE
# ─────────────────────────────────────────────────────────────────────────────
LANDING = HEAD("GoDirect247 — Funeral Cover & Family Protection", 0) + """
<body class="bg-white text-dark">

<nav class="fixed top-0 inset-x-0 z-50 bg-dark/95 backdrop-blur border-b border-white/10">
  <div class="max-w-6xl mx-auto px-5 h-16 flex items-center justify-between">
    <a href="index.html" class="font-display font-extrabold text-white text-xl tracking-tight">Go<span class="text-gold">Direct</span>247</a>
    <div class="hidden md:flex items-center gap-8 text-sm font-medium">
      <a href="#plans" class="text-white/60 hover:text-white transition-colors">Plans</a>
      <a href="#how-it-works" class="text-white/60 hover:text-white transition-colors">How it works</a>
      <a href="#benefits" class="text-white/60 hover:text-white transition-colors">Benefits</a>
    </div>
    <div class="hidden md:flex items-center gap-3">
      <a href="dashboard/index.html" class="text-white/70 hover:text-white text-sm font-medium px-4 py-2">Login</a>
      <a href="signup/index.html" class="bg-gold text-dark text-sm font-bold px-5 py-2.5 rounded-full hover:bg-gold-dark transition-colors">Get Started</a>
    </div>
    <button onclick="document.getElementById('mob').classList.toggle('hidden')" class="md:hidden text-white p-1">
      <i class="ph ph-list text-2xl"></i>
    </button>
  </div>
  <div id="mob" class="hidden md:hidden bg-dark border-t border-white/10 px-5 py-5 flex flex-col gap-4 text-sm">
    <a href="#plans" class="text-white/70 py-1">Plans</a>
    <a href="#how-it-works" class="text-white/70 py-1">How it works</a>
    <a href="#benefits" class="text-white/70 py-1">Benefits</a>
    <div class="border-t border-white/10 pt-4 flex flex-col gap-3">
      <a href="dashboard/index.html" class="text-white/70 py-1 text-center">Login</a>
      <a href="signup/index.html" class="bg-gold text-dark font-bold py-3 rounded-full text-center">Get Started</a>
    </div>
  </div>
</nav>

<section class="bg-dark pt-16 min-h-screen flex flex-col justify-center">
  <div class="max-w-6xl mx-auto px-5 py-24 md:py-32">
    <div class="max-w-3xl">
      <div class="ani1 inline-flex items-center gap-2 bg-white/10 border border-white/15 rounded-full px-4 py-1.5 mb-8">
        <i class="ph ph-shield-check text-gold text-sm"></i>
        <span class="text-white/70 text-xs font-medium tracking-wide">FSP Registered &middot; Zarkudu Group &middot; NCR 26091</span>
      </div>
      <h1 class="ani2 font-display text-white text-5xl sm:text-6xl md:text-[78px] font-extrabold leading-none tracking-tight mb-6">
        Protect your<br>family. <span class="text-gold">Earn</span><br>while you cover.
      </h1>
      <p class="ani3 text-white/50 text-lg md:text-xl leading-relaxed max-w-lg mb-10">
        Affordable funeral cover with real cashback rewards. Two plans, six tiers &mdash; peace of mind for your whole family.
      </p>
      <div class="ani4 flex flex-col sm:flex-row gap-3">
        <a href="signup/index.html" class="bg-gold text-dark font-display font-bold text-base px-8 py-4 rounded-full text-center hover:bg-gold-dark transition-all">Choose your plan</a>
        <a href="#how-it-works" class="border-2 border-white/25 text-white font-medium text-base px-8 py-4 rounded-full text-center hover:border-white/50 hover:bg-white/5 transition-all">How it works</a>
      </div>
    </div>
    <div class="ani5 mt-16 grid grid-cols-1 sm:grid-cols-2 gap-4 max-w-2xl">
      <div class="bg-white/[0.06] border border-white/15 rounded-2xl p-5">
        <div class="flex items-center justify-between mb-3">
          <span class="font-display font-bold text-white">Plus Plan</span>
          <span class="bg-sky-900/40 text-sky-300 text-xs font-semibold px-3 py-1 rounded-full border border-sky-700/30">6 Tiers</span>
        </div>
        <p class="text-white/40 text-xs mb-4">Funeral cover &middot; cashback from month 4 &middot; refer &amp; earn</p>
        <div class="flex flex-wrap gap-1.5">
          <span class="bg-white/10 text-white/60 text-xs px-2.5 py-1 rounded-full">Silver</span>
          <span class="bg-white/10 text-white/60 text-xs px-2.5 py-1 rounded-full">Gold</span>
          <span class="bg-white/10 text-white/60 text-xs px-2.5 py-1 rounded-full">Diamond</span>
          <span class="bg-white/10 text-white/60 text-xs px-2.5 py-1 rounded-full">Premier</span>
          <span class="bg-white/10 text-white/60 text-xs px-2.5 py-1 rounded-full">Prestige</span>
          <span class="bg-white/10 text-white/60 text-xs px-2.5 py-1 rounded-full">King</span>
        </div>
      </div>
      <div class="bg-gold/[0.06] border border-gold/25 rounded-2xl p-5">
        <div class="flex items-center justify-between mb-3">
          <span class="font-display font-bold text-white">Gold Plan</span>
          <span class="bg-gold/20 text-gold text-xs font-semibold px-3 py-1 rounded-full border border-gold/30">7 Tiers</span>
        </div>
        <p class="text-white/40 text-xs mb-4">Payout after 6 weeks &middot; cashback every 3 months &middot; refer &amp; earn</p>
        <div class="flex flex-wrap gap-1.5">
          <span class="bg-gold/10 text-gold/70 text-xs px-2.5 py-1 rounded-full">Silver</span>
          <span class="bg-gold/10 text-gold/70 text-xs px-2.5 py-1 rounded-full">Gold</span>
          <span class="bg-gold/10 text-gold/70 text-xs px-2.5 py-1 rounded-full">Diamond</span>
          <span class="bg-gold/10 text-gold/70 text-xs px-2.5 py-1 rounded-full">Premier</span>
          <span class="bg-gold/10 text-gold/70 text-xs px-2.5 py-1 rounded-full">Prestige</span>
          <span class="bg-gold/10 text-gold/70 text-xs px-2.5 py-1 rounded-full">King</span>
          <span class="bg-gold/20 text-gold font-semibold text-xs px-2.5 py-1 rounded-full">Superior</span>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="bg-surface border-b border-gray-200">
  <div class="max-w-6xl mx-auto px-5 py-7">
    <div class="grid grid-cols-2 md:grid-cols-4 gap-6 text-center">
      <div class="flex flex-col items-center gap-1.5"><i class="ph ph-users text-brand text-2xl"></i><span class="font-display font-bold text-dark text-lg">1 000+</span><span class="text-muted text-xs">Families covered</span></div>
      <div class="flex flex-col items-center gap-1.5"><i class="ph ph-certificate text-brand text-2xl"></i><span class="font-display font-bold text-dark text-lg">FSP Reg.</span><span class="text-muted text-xs">NCR 26091</span></div>
      <div class="flex flex-col items-center gap-1.5"><i class="ph ph-clock text-brand text-2xl"></i><span class="font-display font-bold text-dark text-lg">24&ndash;48 hrs</span><span class="text-muted text-xs">Claim payout</span></div>
      <div class="flex flex-col items-center gap-1.5"><i class="ph ph-coins text-brand text-2xl"></i><span class="font-display font-bold text-dark text-lg">Cashback</span><span class="text-muted text-xs">Real rewards</span></div>
    </div>
  </div>
</section>

<section id="how-it-works" class="py-24 px-5">
  <div class="max-w-6xl mx-auto">
    <div class="text-center mb-16">
      <span class="text-brand text-sm font-semibold tracking-widest uppercase">Simple process</span>
      <h2 class="font-display font-extrabold text-4xl md:text-5xl text-dark mt-3 tracking-tight">Up and covered in minutes</h2>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-5">
      <div class="bg-surface rounded-2xl p-8 relative overflow-hidden">
        <div class="w-10 h-10 bg-dark rounded-xl flex items-center justify-center mb-6"><span class="font-display font-bold text-white text-sm">01</span></div>
        <h3 class="font-display font-bold text-xl text-dark mb-3">Choose your plan</h3>
        <p class="text-slate text-sm leading-relaxed">Pick Plus or Gold, then the tier that fits your budget. See exactly what&#39;s covered before committing.</p>
        <i class="ph ph-layout text-[80px] text-dark/5 absolute -bottom-2 -right-2"></i>
      </div>
      <div class="bg-surface rounded-2xl p-8 relative overflow-hidden">
        <div class="w-10 h-10 bg-dark rounded-xl flex items-center justify-center mb-6"><span class="font-display font-bold text-white text-sm">02</span></div>
        <h3 class="font-display font-bold text-xl text-dark mb-3">Cover your family</h3>
        <p class="text-slate text-sm leading-relaxed">Add your spouse, up to 4 dependents, and extended family in a few taps. No medicals required.</p>
        <i class="ph ph-users text-[80px] text-dark/5 absolute -bottom-2 -right-2"></i>
      </div>
      <div class="bg-gold rounded-2xl p-8 relative overflow-hidden">
        <div class="w-10 h-10 bg-dark rounded-xl flex items-center justify-center mb-6"><span class="font-display font-bold text-white text-sm">03</span></div>
        <h3 class="font-display font-bold text-xl text-dark mb-3">Activate &amp; earn</h3>
        <p class="text-dark/70 text-sm leading-relaxed">Pay your activation fee and cover starts. Cashback arrives on the 5th of your 4th month.</p>
        <i class="ph ph-rocket-launch text-[80px] text-dark/10 absolute -bottom-2 -right-2"></i>
      </div>
    </div>
  </div>
</section>

<section id="plans" class="bg-dark py-24 px-5">
  <div class="max-w-6xl mx-auto">
    <div class="text-center mb-16">
      <span class="text-gold text-sm font-semibold tracking-widest uppercase">Two plans</span>
      <h2 class="font-display font-extrabold text-4xl md:text-5xl text-white mt-3 tracking-tight">Find the right cover</h2>
      <p class="text-white/50 text-lg mt-4 max-w-xl mx-auto">Both plans include funeral cover and referral earnings. Gold adds quarterly payouts.</p>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
      <div class="bg-white/[0.05] border border-white/10 rounded-2xl p-8">
        <div class="flex items-start justify-between mb-6">
          <div><span class="font-display font-extrabold text-white text-2xl">Plus Plan</span><p class="text-white/40 text-sm mt-1">Cover + cashback rewards</p></div>
          <div class="bg-sky-900/30 border border-sky-700/30 rounded-xl p-2.5"><i class="ph ph-shield text-sky-300 text-xl"></i></div>
        </div>
        <ul class="space-y-3 mb-8 text-sm">
          <li class="flex items-center gap-3 text-white/70"><i class="ph-bold ph-check text-teal flex-shrink-0"></i>Funeral cover for you &amp; family</li>
          <li class="flex items-center gap-3 text-white/70"><i class="ph-bold ph-check text-teal flex-shrink-0"></i>Cashback from month 4</li>
          <li class="flex items-center gap-3 text-white/70"><i class="ph-bold ph-check text-teal flex-shrink-0"></i>Refer &amp; earn commission</li>
          <li class="flex items-center gap-3 text-white/70"><i class="ph-bold ph-check text-teal flex-shrink-0"></i>Up to 4 dependents + spouse</li>
          <li class="flex items-center gap-3 text-white/70"><i class="ph-bold ph-check text-teal flex-shrink-0"></i>No medicals required</li>
          <li class="flex items-center gap-3 text-white/25"><i class="ph-bold ph-x text-white/15 flex-shrink-0"></i>Quarterly payout benefit</li>
        </ul>
        <div class="border-t border-white/10 pt-5 mb-6">
          <p class="text-white/30 text-xs uppercase tracking-wide font-semibold mb-3">Tiers</p>
          <div class="flex flex-wrap gap-2">
            <span class="bg-white/[0.07] text-white/60 text-xs px-3 py-1.5 rounded-full border border-white/10">Silver Plus</span>
            <span class="bg-white/[0.07] text-white/60 text-xs px-3 py-1.5 rounded-full border border-white/10">Gold Plus</span>
            <span class="bg-white/[0.07] text-white/60 text-xs px-3 py-1.5 rounded-full border border-white/10">Diamond Plus</span>
            <span class="bg-white/[0.07] text-white/60 text-xs px-3 py-1.5 rounded-full border border-white/10">Premier Plus</span>
            <span class="bg-white/[0.07] text-white/60 text-xs px-3 py-1.5 rounded-full border border-white/10">Prestige Plus</span>
            <span class="bg-white/[0.07] text-white/60 text-xs px-3 py-1.5 rounded-full border border-white/10">King Plus</span>
          </div>
        </div>
        <a href="signup/index.html?plan=plus" class="block w-full text-center border-2 border-white/20 text-white font-semibold py-3.5 rounded-full hover:border-white/40 hover:bg-white/5 transition-all text-sm">Start with Plus Plan</a>
      </div>
      <div class="bg-gold/[0.07] border border-gold/25 rounded-2xl p-8 relative overflow-hidden">
        <div class="absolute top-5 right-5"><span class="bg-gold text-dark text-xs font-bold px-3 py-1 rounded-full">Most Popular</span></div>
        <div class="flex items-start justify-between mb-6">
          <div><span class="font-display font-extrabold text-white text-2xl">Gold Plan</span><p class="text-white/40 text-sm mt-1">Cover + payouts + cashback</p></div>
          <div class="bg-gold/15 border border-gold/25 rounded-xl p-2.5"><i class="ph ph-crown text-gold text-xl"></i></div>
        </div>
        <ul class="space-y-3 mb-8 text-sm">
          <li class="flex items-center gap-3 text-white/70"><i class="ph-bold ph-check text-teal flex-shrink-0"></i>Funeral cover for you &amp; family</li>
          <li class="flex items-center gap-3 text-white/70"><i class="ph-bold ph-check text-teal flex-shrink-0"></i>Cashback from month 4</li>
          <li class="flex items-center gap-3 text-white/70"><i class="ph-bold ph-check text-teal flex-shrink-0"></i>Refer &amp; earn commission</li>
          <li class="flex items-center gap-3 text-white/70"><i class="ph-bold ph-check text-teal flex-shrink-0"></i>Up to 4 dependents + spouse</li>
          <li class="flex items-center gap-3 text-white/70"><i class="ph-bold ph-check text-teal flex-shrink-0"></i>No medicals required</li>
          <li class="flex items-center gap-3 text-gold font-semibold"><i class="ph-bold ph-check text-gold flex-shrink-0"></i>Payout every 3 months from activation</li>
        </ul>
        <div class="border-t border-white/10 pt-5 mb-6">
          <p class="text-white/30 text-xs uppercase tracking-wide font-semibold mb-3">Tiers</p>
          <div class="flex flex-wrap gap-2">
            <span class="bg-gold/[0.07] text-gold/70 text-xs px-3 py-1.5 rounded-full border border-gold/20">Silver Gold</span>
            <span class="bg-gold/[0.07] text-gold/70 text-xs px-3 py-1.5 rounded-full border border-gold/20">Gold Gold</span>
            <span class="bg-gold/[0.07] text-gold/70 text-xs px-3 py-1.5 rounded-full border border-gold/20">Diamond Gold</span>
            <span class="bg-gold/[0.07] text-gold/70 text-xs px-3 py-1.5 rounded-full border border-gold/20">Premier Gold</span>
            <span class="bg-gold/[0.07] text-gold/70 text-xs px-3 py-1.5 rounded-full border border-gold/20">Prestige Gold</span>
            <span class="bg-gold/[0.07] text-gold/70 text-xs px-3 py-1.5 rounded-full border border-gold/20">King Gold</span>
            <span class="bg-gold/15 text-gold text-xs px-3 py-1.5 rounded-full border border-gold/30 font-semibold">Superior</span>
          </div>
        </div>
        <a href="signup/index.html?plan=gold" class="block w-full text-center bg-gold text-dark font-bold py-3.5 rounded-full hover:bg-gold-dark transition-all text-sm">Start with Gold Plan</a>
      </div>
    </div>
    <div class="bg-white/[0.04] border border-white/10 rounded-2xl p-6">
      <div class="flex items-start gap-4">
        <i class="ph ph-info text-white/30 text-xl flex-shrink-0 mt-0.5"></i>
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-4 text-xs text-white/40 leading-relaxed">
          <span><span class="text-white/60 font-semibold">Waiting period:</span> 6 months natural death. Accidental death covered immediately.</span>
          <span><span class="text-white/60 font-semibold">Cashback:</span> Paid 5th of your 4th month. Gold gets quarterly payouts from week 6.</span>
          <span><span class="text-white/60 font-semibold">Renewal:</span> Renew month 11 to avoid lapse. Double activation = single cashback/year.</span>
        </div>
      </div>
    </div>
  </div>
</section>

<section id="benefits" class="py-24 px-5">
  <div class="max-w-6xl mx-auto">
    <div class="text-center mb-16">
      <span class="text-brand text-sm font-semibold tracking-widest uppercase">Why GoDirect247</span>
      <h2 class="font-display font-extrabold text-4xl md:text-5xl text-dark mt-3 tracking-tight">Everything you need</h2>
    </div>
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-5">
      <div class="p-7 rounded-2xl border border-gray-100 hover:border-gray-200 transition-all"><div class="w-12 h-12 bg-teal/10 rounded-xl flex items-center justify-center mb-5"><i class="ph ph-lightning text-teal text-2xl"></i></div><h3 class="font-display font-bold text-dark text-lg mb-2">Fast claims</h3><p class="text-slate text-sm leading-relaxed">Processed and paid within 24&ndash;48 hours of receiving required documentation.</p></div>
      <div class="p-7 rounded-2xl border border-gray-100 hover:border-gray-200 transition-all"><div class="w-12 h-12 bg-gold/20 rounded-xl flex items-center justify-center mb-5"><i class="ph ph-coins text-yellow-600 text-2xl"></i></div><h3 class="font-display font-bold text-dark text-lg mb-2">Cashback rewards</h3><p class="text-slate text-sm leading-relaxed">Real money back from month 4. Gold members also earn quarterly payouts.</p></div>
      <div class="p-7 rounded-2xl border border-gray-100 hover:border-gray-200 transition-all"><div class="w-12 h-12 bg-brand/10 rounded-xl flex items-center justify-center mb-5"><i class="ph ph-share-network text-brand text-2xl"></i></div><h3 class="font-display font-bold text-dark text-lg mb-2">Refer &amp; earn</h3><p class="text-slate text-sm leading-relaxed">Earn commission for every referral. Not mandatory &mdash; your choice entirely.</p></div>
      <div class="p-7 rounded-2xl border border-gray-100 hover:border-gray-200 transition-all"><div class="w-12 h-12 bg-purple-50 rounded-xl flex items-center justify-center mb-5"><i class="ph ph-users text-purple-500 text-2xl"></i></div><h3 class="font-display font-bold text-dark text-lg mb-2">Full family cover</h3><p class="text-slate text-sm leading-relaxed">Spouse, up to 4 dependents, and extended family all under one policy.</p></div>
      <div class="p-7 rounded-2xl border border-gray-100 hover:border-gray-200 transition-all"><div class="w-12 h-12 bg-teal/10 rounded-xl flex items-center justify-center mb-5"><i class="ph ph-heartbeat text-teal text-2xl"></i></div><h3 class="font-display font-bold text-dark text-lg mb-2">No medicals</h3><p class="text-slate text-sm leading-relaxed">No health exams or questions. Apply in minutes from your phone.</p></div>
      <div class="p-7 rounded-2xl border border-gray-100 hover:border-gray-200 transition-all"><div class="w-12 h-12 bg-gray-100 rounded-xl flex items-center justify-center mb-5"><i class="ph ph-certificate text-dark text-2xl"></i></div><h3 class="font-display font-bold text-dark text-lg mb-2">FSP Registered</h3><p class="text-slate text-sm leading-relaxed">Fully regulated. GoDirect247 is a division of Zarkudu Group, NCR 26091.</p></div>
    </div>
  </div>
</section>

<section class="bg-dark py-24 px-5">
  <div class="max-w-3xl mx-auto text-center">
    <h2 class="font-display font-extrabold text-4xl md:text-5xl text-white tracking-tight mb-5 leading-tight">Ready to protect your family today?</h2>
    <p class="text-white/50 text-lg mb-10">Takes less than 5 minutes. No medicals. Pick the tier that fits your budget.</p>
    <div class="flex flex-col sm:flex-row gap-3 justify-center">
      <a href="signup/index.html" class="bg-gold text-dark font-display font-bold text-base px-10 py-4 rounded-full hover:bg-gold-dark transition-all">Get started now</a>
      <a href="tel:0780187995" class="border-2 border-white/25 text-white font-medium text-base px-10 py-4 rounded-full hover:border-white/50 hover:bg-white/5 transition-all flex items-center justify-center gap-2"><i class="ph ph-phone"></i>078 018 7995</a>
    </div>
  </div>
</section>

<footer class="bg-dark border-t border-white/10 py-12 px-5">
  <div class="max-w-6xl mx-auto">
    <div class="grid grid-cols-1 md:grid-cols-3 gap-10 mb-10">
      <div><div class="font-display font-extrabold text-white text-xl mb-3">Go<span class="text-gold">Direct</span>247</div><p class="text-white/40 text-sm leading-relaxed max-w-xs">A division of Zarkudu Group. FSP Registered, NCR 26091.</p></div>
      <div>
        <p class="text-white/30 text-xs font-semibold uppercase tracking-wider mb-4">Navigation</p>
        <ul class="space-y-2.5 text-sm">
          <li><a href="index.html" class="text-white/50 hover:text-white transition-colors">Home</a></li>
          <li><a href="signup/index.html" class="text-white/50 hover:text-white transition-colors">Get Started</a></li>
          <li><a href="dashboard/index.html" class="text-white/50 hover:text-white transition-colors">Member Login</a></li>
          <li><a href="admin/index.html" class="text-white/50 hover:text-white transition-colors">Admin</a></li>
        </ul>
      </div>
      <div>
        <p class="text-white/30 text-xs font-semibold uppercase tracking-wider mb-4">Contact</p>
        <ul class="space-y-2.5 text-sm text-white/50">
          <li class="flex items-center gap-2"><i class="ph ph-phone text-white/30"></i>078 018 7995</li>
          <li class="flex items-center gap-2"><i class="ph ph-whatsapp-logo text-white/30"></i>067 489 1416 (WhatsApp)</li>
        </ul>
      </div>
    </div>
    <div class="border-t border-white/10 pt-6 flex flex-col sm:flex-row justify-between gap-3 text-xs text-white/30">
      <span>&copy; 2026 GoDirect247 &middot; Zarkudu Group &middot; FSP Registered &middot; NCR 26091</span>
      <span>Platform v2.0</span>
    </div>
  </div>
</footer>
<script>
  document.querySelectorAll('a[href^="#"]').forEach(a=>{
    a.addEventListener('click',e=>{
      e.preventDefault();
      const t=document.querySelector(a.getAttribute('href'));
      if(t)t.scrollIntoView({behavior:'smooth'});
      document.getElementById('mob').classList.add('hidden');
    });
  });
</script>
</body>
</html>"""

# ─────────────────────────────────────────────────────────────────────────────
# SIGNUP — 4-step intelligent onboarding
# ─────────────────────────────────────────────────────────────────────────────
SIGNUP = HEAD("Sign Up — GoDirect247", 1) + """
<body class="bg-dark min-h-screen text-dark">

<!-- mini nav -->
<nav class="fixed top-0 inset-x-0 z-50 bg-dark/95 backdrop-blur border-b border-white/10 h-14 flex items-center px-5">
  <a href="../index.html" class="font-display font-extrabold text-white text-lg">Go<span class="text-gold">Direct</span>247</a>
  <div class="ml-auto text-white/50 text-sm" id="stepLabel">Step 1 of 4</div>
</nav>

<div class="pt-14 min-h-screen flex flex-col">
  <!-- Progress bar -->
  <div class="h-1 bg-white/10">
    <div id="progressBar" class="h-1 bg-gold transition-all duration-500" style="width:25%"></div>
  </div>

  <div class="flex-1 flex flex-col items-center justify-start px-5 py-10 max-w-lg mx-auto w-full">

    <!-- STEP 1: Plan Selection -->
    <div id="step1" class="w-full ani1">
      <h2 class="font-display font-extrabold text-white text-3xl sm:text-4xl mb-2 tracking-tight">Choose your plan</h2>
      <p class="text-white/50 text-sm mb-8">Select the plan type, then the tier that fits your budget.</p>

      <div class="grid grid-cols-2 gap-3 mb-6">
        <button onclick="selectPlanType('plus')" id="btn-plus" class="plan-type-btn border-2 border-white/15 rounded-2xl p-5 text-left transition-all hover:border-white/30">
          <i class="ph ph-shield text-sky-300 text-2xl mb-3 block"></i>
          <div class="font-display font-bold text-white text-base">Plus Plan</div>
          <div class="text-white/40 text-xs mt-1">Cashback from month 4</div>
        </button>
        <button onclick="selectPlanType('gold')" id="btn-gold" class="plan-type-btn border-2 border-white/15 rounded-2xl p-5 text-left transition-all hover:border-gold/40">
          <i class="ph ph-crown text-gold text-2xl mb-3 block"></i>
          <div class="font-display font-bold text-white text-base">Gold Plan</div>
          <div class="text-white/40 text-xs mt-1">Payout every 3 months</div>
        </button>
      </div>

      <!-- Tier selection (shown after plan type selected) -->
      <div id="tierSection" class="hidden mb-6">
        <p class="text-white/50 text-xs uppercase tracking-wide font-semibold mb-3">Select your tier</p>
        <div id="tierGrid" class="grid grid-cols-2 gap-2"></div>
      </div>

      <button onclick="nextStep()" id="step1Next" class="hidden w-full bg-gold text-dark font-display font-bold py-4 rounded-full text-base hover:bg-gold-dark transition-all">
        Continue <i class="ph ph-arrow-right ml-1"></i>
      </button>
    </div>

    <!-- STEP 2: Personal Details -->
    <div id="step2" class="hidden w-full ani1">
      <h2 class="font-display font-extrabold text-white text-3xl sm:text-4xl mb-2 tracking-tight">About you</h2>
      <p class="text-white/50 text-sm mb-8">Just three things to get you started.</p>

      <div class="space-y-4 mb-6">
        <div>
          <label class="text-white/60 text-xs font-semibold uppercase tracking-wide block mb-2">Full name &amp; surname</label>
          <input id="f_name" type="text" placeholder="e.g. Thabo Nkosi" class="w-full bg-white/10 border border-white/15 rounded-xl px-4 py-3.5 text-white placeholder-white/30 text-sm transition-all">
        </div>
        <div>
          <label class="text-white/60 text-xs font-semibold uppercase tracking-wide block mb-2">ID number</label>
          <input id="f_id" type="text" inputmode="numeric" maxlength="13" placeholder="13-digit South African ID" class="w-full bg-white/10 border border-white/15 rounded-xl px-4 py-3.5 text-white placeholder-white/30 text-sm transition-all">
        </div>
        <div>
          <label class="text-white/60 text-xs font-semibold uppercase tracking-wide block mb-2">Email address</label>
          <input id="f_email" type="email" placeholder="you@example.com" class="w-full bg-white/10 border border-white/15 rounded-xl px-4 py-3.5 text-white placeholder-white/30 text-sm transition-all">
        </div>
        <div>
          <label class="text-white/60 text-xs font-semibold uppercase tracking-wide block mb-2">Employment status</label>
          <select id="f_employment" class="w-full bg-white/10 border border-white/15 rounded-xl px-4 py-3.5 text-white text-sm transition-all">
            <option value="" class="bg-dark">Select status</option>
            <option value="Full Time" class="bg-dark">Full Time</option>
            <option value="Part Time" class="bg-dark">Part Time</option>
            <option value="Seasonal" class="bg-dark">Seasonal</option>
            <option value="Grant Recipient" class="bg-dark">Grant Recipient</option>
            <option value="Pensioner" class="bg-dark">Pensioner</option>
          </select>
        </div>
        <div>
          <label class="text-white/60 text-xs font-semibold uppercase tracking-wide block mb-2">How did you hear about us?</label>
          <select id="f_source" class="w-full bg-white/10 border border-white/15 rounded-xl px-4 py-3.5 text-white text-sm transition-all">
            <option value="" class="bg-dark">Select source</option>
            <option value="Facebook" class="bg-dark">Facebook</option>
            <option value="TikTok" class="bg-dark">TikTok</option>
            <option value="Google Ads" class="bg-dark">Google Ads</option>
            <option value="A Friend" class="bg-dark">A Friend</option>
            <option value="A Representative" class="bg-dark">A Representative</option>
            <option value="WhatsApp" class="bg-dark">WhatsApp</option>
          </select>
        </div>
        <div>
          <label class="text-white/60 text-xs font-semibold uppercase tracking-wide block mb-2">Referred by <span class="text-white/30 normal-case font-normal">(optional)</span></label>
          <input id="f_referral" type="text" placeholder="Name of person who referred you" class="w-full bg-white/10 border border-white/15 rounded-xl px-4 py-3.5 text-white placeholder-white/30 text-sm transition-all">
        </div>
      </div>

      <div class="flex gap-3">
        <button onclick="prevStep()" class="flex-shrink-0 border-2 border-white/20 text-white py-4 px-6 rounded-full hover:border-white/40 transition-all text-sm"><i class="ph ph-arrow-left"></i></button>
        <button onclick="nextStep()" class="flex-1 bg-gold text-dark font-display font-bold py-4 rounded-full hover:bg-gold-dark transition-all">Continue <i class="ph ph-arrow-right ml-1"></i></button>
      </div>
    </div>

    <!-- STEP 3: Family Coverage -->
    <div id="step3" class="hidden w-full ani1">
      <h2 class="font-display font-extrabold text-white text-3xl sm:text-4xl mb-2 tracking-tight">Your family</h2>
      <p class="text-white/50 text-sm mb-8">Who are you covering? Add as many as apply.</p>

      <!-- Beneficiary -->
      <div class="mb-5">
        <p class="text-white/60 text-xs font-semibold uppercase tracking-wide mb-3">Main beneficiary</p>
        <div class="bg-white/[0.05] border border-white/10 rounded-2xl p-4 space-y-3">
          <input id="ben_name" type="text" placeholder="Beneficiary full name" class="w-full bg-white/10 border border-white/15 rounded-xl px-4 py-3 text-white placeholder-white/30 text-sm">
          <input id="ben_id" type="text" placeholder="Beneficiary ID number" class="w-full bg-white/10 border border-white/15 rounded-xl px-4 py-3 text-white placeholder-white/30 text-sm">
          <select id="ben_relation" class="w-full bg-white/10 border border-white/15 rounded-xl px-4 py-3 text-white text-sm">
            <option value="" class="bg-dark">Relationship to beneficiary</option>
            <option value="Partner" class="bg-dark">Partner</option>
            <option value="Child" class="bg-dark">Child</option>
            <option value="Parent" class="bg-dark">Parent</option>
            <option value="Other" class="bg-dark">Other</option>
          </select>
        </div>
      </div>

      <!-- Spouse toggle -->
      <div class="mb-5">
        <div class="flex items-center justify-between mb-3">
          <p class="text-white/60 text-xs font-semibold uppercase tracking-wide">Spouse</p>
          <button onclick="toggleSection('spouseSection', this)" class="bg-white/10 text-white/60 text-xs px-3 py-1.5 rounded-full hover:bg-white/20 transition-all">+ Add spouse</button>
        </div>
        <div id="spouseSection" class="hidden bg-white/[0.05] border border-white/10 rounded-2xl p-4 space-y-3">
          <input id="sp_name" type="text" placeholder="Spouse first name" class="w-full bg-white/10 border border-white/15 rounded-xl px-4 py-3 text-white placeholder-white/30 text-sm">
          <input id="sp_surname" type="text" placeholder="Spouse surname" class="w-full bg-white/10 border border-white/15 rounded-xl px-4 py-3 text-white placeholder-white/30 text-sm">
          <input id="sp_id" type="text" placeholder="Spouse ID number" class="w-full bg-white/10 border border-white/15 rounded-xl px-4 py-3 text-white placeholder-white/30 text-sm">
          <input id="sp_cell" type="tel" placeholder="Spouse cell number" class="w-full bg-white/10 border border-white/15 rounded-xl px-4 py-3 text-white placeholder-white/30 text-sm">
        </div>
      </div>

      <!-- Dependents -->
      <div class="mb-5">
        <div class="flex items-center justify-between mb-3">
          <p class="text-white/60 text-xs font-semibold uppercase tracking-wide">Dependents <span class="text-white/30 normal-case font-normal">(up to 4)</span></p>
          <button onclick="addDependent()" id="addDepBtn" class="bg-white/10 text-white/60 text-xs px-3 py-1.5 rounded-full hover:bg-white/20 transition-all">+ Add dependent</button>
        </div>
        <div id="dependentsContainer" class="space-y-3"></div>
      </div>

      <!-- Extended family toggle -->
      <div class="mb-6">
        <div class="flex items-center justify-between mb-3">
          <p class="text-white/60 text-xs font-semibold uppercase tracking-wide">Extended family <span class="text-white/30 normal-case font-normal">(optional)</span></p>
          <button onclick="toggleSection('extSection', this)" class="bg-white/10 text-white/60 text-xs px-3 py-1.5 rounded-full hover:bg-white/20 transition-all">+ Add</button>
        </div>
        <div id="extSection" class="hidden bg-white/[0.05] border border-white/10 rounded-2xl p-4 space-y-3">
          <input id="ext_name" type="text" placeholder="Extended family full name" class="w-full bg-white/10 border border-white/15 rounded-xl px-4 py-3 text-white placeholder-white/30 text-sm">
          <input id="ext_id" type="text" placeholder="Extended family ID number" class="w-full bg-white/10 border border-white/15 rounded-xl px-4 py-3 text-white placeholder-white/30 text-sm">
        </div>
      </div>

      <div class="flex gap-3">
        <button onclick="prevStep()" class="flex-shrink-0 border-2 border-white/20 text-white py-4 px-6 rounded-full hover:border-white/40 transition-all text-sm"><i class="ph ph-arrow-left"></i></button>
        <button onclick="nextStep()" class="flex-1 bg-gold text-dark font-display font-bold py-4 rounded-full hover:bg-gold-dark transition-all">Review application <i class="ph ph-arrow-right ml-1"></i></button>
      </div>
    </div>

    <!-- STEP 4: Review & Submit -->
    <div id="step4" class="hidden w-full ani1">
      <h2 class="font-display font-extrabold text-white text-3xl sm:text-4xl mb-2 tracking-tight">Review &amp; submit</h2>
      <p class="text-white/50 text-sm mb-8">Check your details before submitting.</p>

      <div id="reviewCard" class="bg-white/[0.05] border border-white/10 rounded-2xl p-5 mb-5 space-y-4 text-sm"></div>

      <!-- T&Cs -->
      <div class="bg-white/[0.04] border border-white/10 rounded-2xl p-4 mb-5 max-h-40 overflow-y-auto text-xs text-white/40 leading-relaxed">
        <p class="font-semibold text-white/60 mb-2">Key Terms &amp; Conditions</p>
        A 6-month waiting period applies for natural death. Accidental death covered immediately. A 12-month waiting period applies for suicide. Cashback is payable on the 5th day of the 4th month from activation. Gold Plan payouts are payable after 6 weeks from activation. Renewal must be done on the 11th month to avoid policy lapse. Early withdrawal is payable at 10% (full amount lapses). No advance requests for cashback or payout will be granted. Activation date means the date you paid for your policy, not the date you submitted your application.
      </div>

      <label class="flex items-start gap-3 cursor-pointer mb-6">
        <input id="tcCheck" type="checkbox" class="mt-0.5 w-4 h-4 accent-gold flex-shrink-0">
        <span class="text-white/60 text-sm">I have read and accept the terms &amp; conditions above</span>
      </label>

      <div class="flex gap-3">
        <button onclick="prevStep()" class="flex-shrink-0 border-2 border-white/20 text-white py-4 px-6 rounded-full hover:border-white/40 transition-all text-sm"><i class="ph ph-arrow-left"></i></button>
        <button onclick="submitApp()" class="flex-1 bg-gold text-dark font-display font-bold py-4 rounded-full hover:bg-gold-dark transition-all">Submit application <i class="ph ph-paper-plane-right ml-1"></i></button>
      </div>
    </div>

    <!-- SUCCESS -->
    <div id="stepSuccess" class="hidden w-full text-center ani1">
      <div class="w-20 h-20 bg-teal/20 rounded-full flex items-center justify-center mx-auto mb-6">
        <i class="ph ph-check-circle text-teal text-4xl"></i>
      </div>
      <h2 class="font-display font-extrabold text-white text-3xl mb-3">Application submitted!</h2>
      <p class="text-white/50 text-sm leading-relaxed mb-8 max-w-sm mx-auto">We&#39;ve received your application. Keep an eye on your phone &mdash; we&#39;ll send you a message to confirm your policy. Your cover activates on your payment date.</p>
      <a href="../index.html" class="inline-block border-2 border-white/25 text-white font-medium px-8 py-3.5 rounded-full hover:border-white/50 hover:bg-white/5 transition-all text-sm">Back to home</a>
    </div>

  </div>
</div>

<script>
const PLUS_TIERS = ['Silver Plus','Gold Plus','Diamond Plus','Premier Plus','Prestige Plus','King Plus'];
const GOLD_TIERS = ['Silver Gold','Gold Gold','Diamond Gold','Premier Gold','Prestige Gold','King Gold','Superior'];

let currentStep = 1;
let selectedPlan = '';
let selectedTier = '';
let depCount = 0;

// Check URL param for pre-selected plan
const urlPlan = new URLSearchParams(location.search).get('plan');
if(urlPlan) { setTimeout(()=>selectPlanType(urlPlan),100); }

function selectPlanType(type) {
  selectedPlan = type;
  selectedTier = '';
  const btnPlus = document.getElementById('btn-plus');
  const btnGold = document.getElementById('btn-gold');
  if(type==='plus') {
    btnPlus.classList.add('border-brand','bg-sky-900/20');
    btnPlus.classList.remove('border-white/15');
    btnGold.classList.remove('border-gold/40','bg-gold/5');
    btnGold.classList.add('border-white/15');
  } else {
    btnGold.classList.add('border-gold/40','bg-gold/5');
    btnGold.classList.remove('border-white/15');
    btnPlus.classList.remove('border-brand','bg-sky-900/20');
    btnPlus.classList.add('border-white/15');
  }
  const tiers = type==='plus' ? PLUS_TIERS : GOLD_TIERS;
  const grid = document.getElementById('tierGrid');
  grid.innerHTML = tiers.map(t => `<button onclick="selectTier('${t}',this)" class="tier-btn border border-white/15 rounded-xl py-3 px-3 text-white/60 text-xs font-semibold hover:border-gold/40 hover:text-white transition-all">${t}</button>`).join('');
  document.getElementById('tierSection').classList.remove('hidden');
  document.getElementById('step1Next').classList.add('hidden');
}

function selectTier(tier, btn) {
  selectedTier = tier;
  document.querySelectorAll('.tier-btn').forEach(b=>{ b.classList.remove('border-gold','text-gold','bg-gold/10'); b.classList.add('border-white/15','text-white/60'); });
  btn.classList.add('border-gold','text-gold','bg-gold/10');
  btn.classList.remove('border-white/15','text-white/60');
  document.getElementById('step1Next').classList.remove('hidden');
}

function toggleSection(id, btn) {
  const el = document.getElementById(id);
  const hidden = el.classList.contains('hidden');
  el.classList.toggle('hidden');
  btn.textContent = hidden ? '- Remove' : (id==='spouseSection' ? '+ Add spouse' : '+ Add');
}

function addDependent() {
  if(depCount >= 4) return;
  depCount++;
  const c = document.getElementById('dependentsContainer');
  const div = document.createElement('div');
  div.id = 'dep'+depCount;
  div.className = 'bg-white/[0.05] border border-white/10 rounded-2xl p-4 space-y-3';
  div.innerHTML = `
    <div class="flex items-center justify-between"><span class="text-white/50 text-xs font-semibold">Dependent ${depCount}</span><button onclick="removeDependent(${depCount})" class="text-danger/60 hover:text-danger text-xs"><i class="ph ph-x"></i> Remove</button></div>
    <input type="text" placeholder="Full name" class="w-full bg-white/10 border border-white/15 rounded-xl px-4 py-3 text-white placeholder-white/30 text-sm" data-dep="${depCount}" data-field="name">
    <input type="text" placeholder="Relationship (e.g. Son, Daughter)" class="w-full bg-white/10 border border-white/15 rounded-xl px-4 py-3 text-white placeholder-white/30 text-sm" data-dep="${depCount}" data-field="relation">
    <input type="text" placeholder="ID number" class="w-full bg-white/10 border border-white/15 rounded-xl px-4 py-3 text-white placeholder-white/30 text-sm" data-dep="${depCount}" data-field="id">`;
  c.appendChild(div);
  if(depCount>=4) document.getElementById('addDepBtn').classList.add('opacity-40','pointer-events-none');
}

function removeDependent(n) {
  document.getElementById('dep'+n)?.remove();
  if(depCount>=4) { document.getElementById('addDepBtn').classList.remove('opacity-40','pointer-events-none'); }
  depCount = Math.max(0, depCount-1);
}

function nextStep() {
  if(currentStep===1 && (!selectedPlan || !selectedTier)) return;
  if(currentStep===2) {
    const name=document.getElementById('f_name').value.trim();
    const id=document.getElementById('f_id').value.trim();
    const email=document.getElementById('f_email').value.trim();
    if(!name||!id||!email) { alert('Please fill in your name, ID number and email.'); return; }
  }
  if(currentStep===4) return;
  document.getElementById('step'+currentStep).classList.add('hidden');
  currentStep++;
  if(currentStep===4) buildReview();
  document.getElementById('step'+currentStep).classList.remove('hidden');
  document.getElementById('step'+currentStep).classList.add('ani1');
  updateProgress();
  window.scrollTo(0,0);
}

function prevStep() {
  document.getElementById('step'+currentStep).classList.add('hidden');
  currentStep--;
  document.getElementById('step'+currentStep).classList.remove('hidden');
  updateProgress();
  window.scrollTo(0,0);
}

function updateProgress() {
  const pct = (currentStep/4)*100;
  document.getElementById('progressBar').style.width = pct+'%';
  document.getElementById('stepLabel').textContent = 'Step '+currentStep+' of 4';
}

function buildReview() {
  const rows = [
    ['Plan', selectedTier + ' (' + selectedPlan.charAt(0).toUpperCase()+selectedPlan.slice(1)+' Plan)'],
    ['Applicant', document.getElementById('f_name').value],
    ['ID Number', document.getElementById('f_id').value],
    ['Email', document.getElementById('f_email').value],
    ['Employment', document.getElementById('f_employment').value || 'Not specified'],
    ['Referred by', document.getElementById('f_referral').value || 'N/A'],
    ['Beneficiary', document.getElementById('ben_name').value || 'Not added'],
  ];
  const sp = document.getElementById('sp_name').value;
  if(sp) rows.push(['Spouse', sp+' '+document.getElementById('sp_surname').value]);
  const card = document.getElementById('reviewCard');
  card.innerHTML = rows.map(([k,v])=>`
    <div class="flex justify-between items-start gap-4">
      <span class="text-white/40 text-xs uppercase tracking-wide font-semibold flex-shrink-0">${k}</span>
      <span class="text-white text-right">${v}</span>
    </div>`).join('<div class="border-t border-white/10"></div>');
}

function submitApp() {
  if(!document.getElementById('tcCheck').checked) { alert('Please accept the terms and conditions.'); return; }
  document.getElementById('step4').classList.add('hidden');
  document.getElementById('stepSuccess').classList.remove('hidden');
  document.getElementById('progressBar').style.width='100%';
  document.getElementById('stepLabel').textContent='Done';
  window.scrollTo(0,0);
}
</script>
</body>
</html>"""

# ─────────────────────────────────────────────────────────────────────────────
# MEMBER DASHBOARD
# ─────────────────────────────────────────────────────────────────────────────
DASHBOARD = HEAD("My Dashboard — GoDirect247", 1) + """
<body class="bg-dark min-h-screen text-dark">

<!-- Top bar -->
<nav class="fixed top-0 inset-x-0 z-50 bg-dark border-b border-white/10 h-14 flex items-center px-5 gap-3">
  <div class="font-display font-extrabold text-white text-lg">Go<span class="text-gold">Direct</span>247</div>
  <div class="ml-auto flex items-center gap-3">
    <div class="w-8 h-8 rounded-full bg-gold/20 border border-gold/30 flex items-center justify-center">
      <i class="ph ph-user text-gold text-sm"></i>
    </div>
  </div>
</nav>

<div class="pt-14 max-w-lg mx-auto px-4 py-6">

  <!-- Greeting -->
  <div class="ani1 mb-6">
    <p class="text-white/40 text-sm">Good morning,</p>
    <h1 class="font-display font-extrabold text-white text-2xl">Thabo Nkosi</h1>
  </div>

  <!-- Policy status card -->
  <div class="ani2 bg-gold rounded-2xl p-5 mb-4">
    <div class="flex items-start justify-between mb-4">
      <div>
        <p class="text-dark/60 text-xs font-semibold uppercase tracking-wide">Your plan</p>
        <p class="font-display font-extrabold text-dark text-xl mt-0.5">Gold Plus</p>
      </div>
      <span class="bg-dark/15 text-dark font-bold text-xs px-3 py-1.5 rounded-full">Active</span>
    </div>
    <div class="grid grid-cols-2 gap-4 text-dark/70 text-xs">
      <div><p class="font-semibold text-dark">21 Apr 2026</p><p>Activation date</p></div>
      <div><p class="font-semibold text-dark">21 Mar 2027</p><p>Renewal due</p></div>
    </div>
  </div>

  <!-- Cashback countdown -->
  <div class="ani2 bg-white/[0.05] border border-white/10 rounded-2xl p-5 mb-4">
    <div class="flex items-center justify-between mb-4">
      <div class="flex items-center gap-2">
        <i class="ph ph-coins text-gold text-xl"></i>
        <span class="font-display font-bold text-white text-base">Cashback tracker</span>
      </div>
      <span class="text-white/40 text-xs">Gold Plan</span>
    </div>
    <div class="mb-3">
      <div class="flex justify-between text-xs text-white/40 mb-1.5">
        <span>Progress to cashback</span>
        <span class="text-white font-semibold">Day 1 of 120</span>
      </div>
      <div class="h-2 bg-white/10 rounded-full overflow-hidden">
        <div class="h-2 bg-gold rounded-full" style="width:1%"></div>
      </div>
    </div>
    <p class="text-white/50 text-xs">First cashback on <span class="text-white font-semibold">21 Aug 2026</span> (5th of your 4th month)</p>
    <div class="mt-3 pt-3 border-t border-white/10">
      <p class="text-white/50 text-xs">Next quarterly payout after <span class="text-gold font-semibold">6 weeks</span> from activation</p>
    </div>
  </div>

  <!-- Family covered -->
  <div class="ani3 bg-white/[0.05] border border-white/10 rounded-2xl p-5 mb-4">
    <div class="flex items-center justify-between mb-4">
      <div class="flex items-center gap-2">
        <i class="ph ph-users text-sky-300 text-xl"></i>
        <span class="font-display font-bold text-white text-base">Family covered</span>
      </div>
      <span class="bg-teal/20 text-teal text-xs font-semibold px-2.5 py-1 rounded-full">3 members</span>
    </div>
    <div class="space-y-3">
      <div class="flex items-center justify-between">
        <div class="flex items-center gap-3">
          <div class="w-8 h-8 bg-white/10 rounded-full flex items-center justify-center"><i class="ph ph-user text-white/60 text-sm"></i></div>
          <div><p class="text-white text-sm font-semibold">You (main member)</p><p class="text-white/40 text-xs">Gold Plus</p></div>
        </div>
        <i class="ph ph-check-circle text-teal text-lg"></i>
      </div>
      <div class="flex items-center justify-between">
        <div class="flex items-center gap-3">
          <div class="w-8 h-8 bg-white/10 rounded-full flex items-center justify-center"><i class="ph ph-user text-white/60 text-sm"></i></div>
          <div><p class="text-white text-sm font-semibold">Nomsa Nkosi</p><p class="text-white/40 text-xs">Spouse</p></div>
        </div>
        <i class="ph ph-check-circle text-teal text-lg"></i>
      </div>
      <div class="flex items-center justify-between">
        <div class="flex items-center gap-3">
          <div class="w-8 h-8 bg-white/10 rounded-full flex items-center justify-center"><i class="ph ph-user text-white/60 text-sm"></i></div>
          <div><p class="text-white text-sm font-semibold">Lebo Nkosi</p><p class="text-white/40 text-xs">Dependent &middot; Child</p></div>
        </div>
        <i class="ph ph-check-circle text-teal text-lg"></i>
      </div>
    </div>
  </div>

  <!-- Quick actions -->
  <div class="ani4 grid grid-cols-2 gap-3 mb-4">
    <button class="bg-white/[0.05] border border-white/10 rounded-2xl p-4 text-left hover:border-white/20 transition-all">
      <i class="ph ph-phone-call text-sky-300 text-2xl mb-3 block"></i>
      <p class="font-display font-bold text-white text-sm">Contact support</p>
      <p class="text-white/40 text-xs mt-0.5">078 018 7995</p>
    </button>
    <button class="bg-white/[0.05] border border-white/10 rounded-2xl p-4 text-left hover:border-white/20 transition-all">
      <i class="ph ph-share-network text-gold text-2xl mb-3 block"></i>
      <p class="font-display font-bold text-white text-sm">Refer &amp; earn</p>
      <p class="text-white/40 text-xs mt-0.5">Share your link</p>
    </button>
  </div>

  <!-- Waiting period notice -->
  <div class="ani4 bg-white/[0.04] border border-white/10 rounded-2xl p-4 mb-4">
    <div class="flex items-start gap-3">
      <i class="ph ph-warning text-gold text-xl flex-shrink-0 mt-0.5"></i>
      <div>
        <p class="text-white font-semibold text-sm mb-1">Waiting period active</p>
        <p class="text-white/50 text-xs leading-relaxed">Your 6-month natural death waiting period ends on <span class="text-white font-semibold">21 Oct 2026</span>. Accidental death is covered immediately.</p>
      </div>
    </div>
  </div>

  <!-- Sign out -->
  <button onclick="alert('Sign out — connect to Firebase Auth')" class="w-full border border-white/10 text-white/40 text-sm py-3.5 rounded-xl hover:border-white/20 hover:text-white/60 transition-all flex items-center justify-center gap-2">
    <i class="ph ph-sign-out"></i> Sign out
  </button>

</div>
</body>
</html>"""

# ─────────────────────────────────────────────────────────────────────────────
# ADMIN LOGIN
# ─────────────────────────────────────────────────────────────────────────────
ADMIN_LOGIN = HEAD("Admin Login — GoDirect247", 1) + """
<body class="bg-dark min-h-screen flex items-center justify-center px-5">
<div class="w-full max-w-sm">
  <div class="text-center mb-10 ani1">
    <div class="font-display font-extrabold text-white text-2xl mb-1">Go<span class="text-gold">Direct</span>247</div>
    <p class="text-white/40 text-sm">Admin portal</p>
  </div>
  <div class="ani2 bg-white/[0.06] border border-white/10 rounded-2xl p-7">
    <h1 class="font-display font-extrabold text-white text-xl mb-6">Sign in</h1>
    <div class="space-y-4 mb-6">
      <div>
        <label class="text-white/50 text-xs font-semibold uppercase tracking-wide block mb-2">Email</label>
        <input type="email" placeholder="admin@godirect247.co.za" class="w-full bg-white/10 border border-white/15 rounded-xl px-4 py-3.5 text-white placeholder-white/30 text-sm">
      </div>
      <div>
        <label class="text-white/50 text-xs font-semibold uppercase tracking-wide block mb-2">Password</label>
        <input type="password" placeholder="&bull;&bull;&bull;&bull;&bull;&bull;&bull;&bull;" class="w-full bg-white/10 border border-white/15 rounded-xl px-4 py-3.5 text-white placeholder-white/30 text-sm">
      </div>
    </div>
    <a href="dashboard.html" class="block w-full text-center bg-gold text-dark font-display font-bold py-4 rounded-full hover:bg-gold-dark transition-all text-sm">Sign in to admin</a>
  </div>
  <p class="text-center text-white/30 text-xs mt-6"><a href="../index.html" class="hover:text-white/60 transition-colors">Back to website</a></p>
</div>
</body>
</html>"""

# ─────────────────────────────────────────────────────────────────────────────
# ADMIN DASHBOARD
# ─────────────────────────────────────────────────────────────────────────────
ADMIN_DASH = HEAD("Admin Dashboard — GoDirect247", 1) + """
<body class="bg-[#111315] min-h-screen text-dark">

<!-- Top bar -->
<nav class="fixed top-0 inset-x-0 z-50 bg-dark border-b border-white/10 h-14 flex items-center px-5 gap-3">
  <div class="font-display font-extrabold text-white text-lg">Go<span class="text-gold">Direct</span>247 <span class="text-white/30 font-normal text-sm ml-1">Admin</span></div>
  <div class="ml-auto flex items-center gap-3">
    <span class="text-white/50 text-sm hidden sm:block">admin@godirect247.co.za</span>
    <button onclick="if(confirm('Sign out?'))location.href='index.html'" class="text-white/40 hover:text-white transition-colors p-1"><i class="ph ph-sign-out text-lg"></i></button>
  </div>
</nav>

<div class="pt-14 max-w-6xl mx-auto px-4 py-8">

  <!-- Stats -->
  <div class="ani1 grid grid-cols-2 lg:grid-cols-4 gap-4 mb-8">
    <div class="bg-dark border border-white/10 rounded-2xl p-5">
      <p class="text-white/40 text-xs uppercase tracking-wide font-semibold mb-1">Total members</p>
      <p class="font-display font-extrabold text-white text-3xl">1 247</p>
      <p class="text-teal text-xs mt-1 flex items-center gap-1"><i class="ph ph-trend-up"></i> +23 this month</p>
    </div>
    <div class="bg-dark border border-white/10 rounded-2xl p-5">
      <p class="text-white/40 text-xs uppercase tracking-wide font-semibold mb-1">Active policies</p>
      <p class="font-display font-extrabold text-white text-3xl">1 089</p>
      <p class="text-white/40 text-xs mt-1">87% activation rate</p>
    </div>
    <div class="bg-dark border border-white/10 rounded-2xl p-5">
      <p class="text-white/40 text-xs uppercase tracking-wide font-semibold mb-1">Pending review</p>
      <p class="font-display font-extrabold text-gold text-3xl">47</p>
      <p class="text-white/40 text-xs mt-1">Awaiting activation</p>
    </div>
    <div class="bg-dark border border-white/10 rounded-2xl p-5">
      <p class="text-white/40 text-xs uppercase tracking-wide font-semibold mb-1">This month</p>
      <p class="font-display font-extrabold text-white text-3xl">23</p>
      <p class="text-white/40 text-xs mt-1">New applications</p>
    </div>
  </div>

  <!-- Filters + search -->
  <div class="ani2 bg-dark border border-white/10 rounded-2xl overflow-hidden">
    <div class="p-5 border-b border-white/10 flex flex-col sm:flex-row gap-3">
      <div class="flex-1 relative">
        <i class="ph ph-magnifying-glass text-white/30 absolute left-3.5 top-1/2 -translate-y-1/2 text-lg"></i>
        <input id="searchInput" type="text" placeholder="Search by name, ID or email..." oninput="filterTable()" class="w-full bg-white/10 border border-white/15 rounded-xl pl-10 pr-4 py-2.5 text-white placeholder-white/30 text-sm">
      </div>
      <select id="statusFilter" onchange="filterTable()" class="bg-white/10 border border-white/15 rounded-xl px-4 py-2.5 text-white text-sm">
        <option value="" class="bg-dark">All status</option>
        <option value="Active" class="bg-dark">Active</option>
        <option value="Pending" class="bg-dark">Pending</option>
        <option value="Lapsed" class="bg-dark">Lapsed</option>
      </select>
      <select id="planFilter" onchange="filterTable()" class="bg-white/10 border border-white/15 rounded-xl px-4 py-2.5 text-white text-sm">
        <option value="" class="bg-dark">All plans</option>
        <option value="Plus" class="bg-dark">Plus Plan</option>
        <option value="Gold" class="bg-dark">Gold Plan</option>
      </select>
    </div>

    <!-- Table (desktop) / Cards (mobile) -->
    <div class="hidden sm:block overflow-x-auto">
      <table class="w-full text-sm">
        <thead>
          <tr class="border-b border-white/10">
            <th class="text-left text-white/30 text-xs uppercase tracking-wide font-semibold px-5 py-3">Member</th>
            <th class="text-left text-white/30 text-xs uppercase tracking-wide font-semibold px-5 py-3">Plan</th>
            <th class="text-left text-white/30 text-xs uppercase tracking-wide font-semibold px-5 py-3">Status</th>
            <th class="text-left text-white/30 text-xs uppercase tracking-wide font-semibold px-5 py-3">Applied</th>
            <th class="text-left text-white/30 text-xs uppercase tracking-wide font-semibold px-5 py-3">Action</th>
          </tr>
        </thead>
        <tbody id="membersTable">
        </tbody>
      </table>
    </div>

    <!-- Mobile cards -->
    <div id="mobileCards" class="sm:hidden divide-y divide-white/5"></div>

    <div class="p-4 border-t border-white/10 text-white/30 text-xs" id="tableFooter">Showing all members</div>
  </div>
</div>

<!-- Member detail drawer -->
<div id="drawer" class="fixed inset-0 z-50 hidden">
  <div onclick="closeDrawer()" class="absolute inset-0 bg-black/60 backdrop-blur-sm"></div>
  <div class="absolute right-0 top-0 bottom-0 w-full max-w-md bg-dark border-l border-white/10 overflow-y-auto">
    <div class="p-5 border-b border-white/10 flex items-center justify-between sticky top-0 bg-dark z-10">
      <h2 class="font-display font-bold text-white text-lg" id="drawerName">Member</h2>
      <button onclick="closeDrawer()" class="text-white/40 hover:text-white p-1"><i class="ph ph-x text-xl"></i></button>
    </div>
    <div id="drawerContent" class="p-5 space-y-4"></div>
  </div>
</div>

<script>
const MEMBERS = [
  {id:1,name:'Thabo Nkosi',email:'thabo@email.com',idno:'9001015001089',plan:'Gold Plus',status:'Active',applied:'21 Apr 2026',dep:2,referral:'Sarah M.'},
  {id:2,name:'Nomvula Dlamini',email:'nomvula@email.com',idno:'8803220200085',plan:'Silver Plus',status:'Pending',applied:'20 Apr 2026',dep:1,referral:''},
  {id:3,name:'Sipho Khumalo',email:'sipho@email.com',idno:'9204050301080',plan:'Diamond Gold',status:'Active',applied:'18 Apr 2026',dep:3,referral:'Thabo N.'},
  {id:4,name:'Zanele Mokoena',email:'zanele@email.com',idno:'8507150400080',plan:'King Plus',status:'Active',applied:'15 Apr 2026',dep:4,referral:''},
  {id:5,name:'Bongani Zulu',email:'bongani@email.com',idno:'9112280500088',plan:'Superior',status:'Pending',applied:'12 Apr 2026',dep:2,referral:'Rep: Sipho K.'},
  {id:6,name:'Lindiwe Ntuli',email:'lindiwe@email.com',idno:'8705160600082',plan:'Gold Gold',status:'Lapsed',applied:'01 Mar 2026',dep:1,referral:''},
  {id:7,name:'Mpho Sithole',email:'mpho@email.com',idno:'9309070700087',plan:'Premier Plus',status:'Active',applied:'28 Mar 2026',dep:2,referral:'Ad: Facebook'},
  {id:8,name:'Ayanda Cele',email:'ayanda@email.com',idno:'8801230800089',plan:'Silver Gold',status:'Pending',applied:'22 Apr 2026',dep:0,referral:''},
];

const STATUS_COLORS = {Active:'text-teal bg-teal/10 border-teal/20',Pending:'text-gold bg-gold/10 border-gold/20',Lapsed:'text-danger bg-danger/10 border-danger/20'};

function statusBadge(s){return `<span class="text-xs font-semibold px-2.5 py-1 rounded-full border ${STATUS_COLORS[s]||''}">${s}</span>`;}

function renderTable(data) {
  // Desktop table
  document.getElementById('membersTable').innerHTML = data.map(m=>`
    <tr class="border-b border-white/5 hover:bg-white/[0.03] cursor-pointer transition-colors" onclick="openDrawer(${m.id})">
      <td class="px-5 py-3.5">
        <div class="font-semibold text-white text-sm">${m.name}</div>
        <div class="text-white/40 text-xs">${m.email}</div>
      </td>
      <td class="px-5 py-3.5 text-white/70 text-sm">${m.plan}</td>
      <td class="px-5 py-3.5">${statusBadge(m.status)}</td>
      <td class="px-5 py-3.5 text-white/40 text-xs">${m.applied}</td>
      <td class="px-5 py-3.5">
        <button onclick="event.stopPropagation();changeStatus(${m.id})" class="text-white/40 hover:text-white text-xs border border-white/15 rounded-full px-3 py-1 hover:border-white/30 transition-all">Update</button>
      </td>
    </tr>`).join('');
  // Mobile cards
  document.getElementById('mobileCards').innerHTML = data.map(m=>`
    <div class="p-4 flex items-center justify-between cursor-pointer hover:bg-white/[0.03] transition-colors" onclick="openDrawer(${m.id})">
      <div>
        <div class="font-semibold text-white text-sm">${m.name}</div>
        <div class="text-white/40 text-xs mt-0.5">${m.plan} &middot; ${m.applied}</div>
      </div>
      <div class="flex items-center gap-2">${statusBadge(m.status)}<i class="ph ph-caret-right text-white/30"></i></div>
    </div>`).join('');
  document.getElementById('tableFooter').textContent = `Showing ${data.length} of ${MEMBERS.length} members`;
}

function filterTable() {
  const q = document.getElementById('searchInput').value.toLowerCase();
  const st = document.getElementById('statusFilter').value;
  const pl = document.getElementById('planFilter').value;
  const filtered = MEMBERS.filter(m=>{
    const matchQ = !q || m.name.toLowerCase().includes(q) || m.email.toLowerCase().includes(q) || m.idno.includes(q);
    const matchS = !st || m.status===st;
    const matchP = !pl || m.plan.includes(pl);
    return matchQ && matchS && matchP;
  });
  renderTable(filtered);
}

function openDrawer(id) {
  const m = MEMBERS.find(x=>x.id===id);
  if(!m) return;
  document.getElementById('drawerName').textContent = m.name;
  document.getElementById('drawerContent').innerHTML = `
    <div class="bg-white/[0.05] border border-white/10 rounded-2xl p-4 space-y-3">
      ${[['Status',statusBadge(m.status)],['Plan',`<span class="text-white">${m.plan}</span>`],['ID Number',`<span class="text-white/70">${m.idno}</span>`],['Email',`<span class="text-white/70">${m.email}</span>`],['Applied',`<span class="text-white/70">${m.applied}</span>`],['Dependents',`<span class="text-white/70">${m.dep}</span>`],['Referral',`<span class="text-white/70">${m.referral||'None'}</span>`]]
        .map(([k,v])=>`<div class="flex items-center justify-between gap-4"><span class="text-white/40 text-xs uppercase tracking-wide font-semibold">${k}</span>${v}</div>`)
        .join('<div class="border-t border-white/5"></div>')}
    </div>
    <div class="grid grid-cols-3 gap-2">
      <button onclick="setStatus(${id},'Active')" class="bg-teal/10 border border-teal/20 text-teal text-xs font-semibold py-2.5 rounded-xl hover:bg-teal/20 transition-all">Activate</button>
      <button onclick="setStatus(${id},'Pending')" class="bg-gold/10 border border-gold/20 text-gold text-xs font-semibold py-2.5 rounded-xl hover:bg-gold/20 transition-all">Pending</button>
      <button onclick="setStatus(${id},'Lapsed')" class="bg-danger/10 border border-danger/20 text-danger text-xs font-semibold py-2.5 rounded-xl hover:bg-danger/20 transition-all">Lapse</button>
    </div>
    <div>
      <label class="text-white/40 text-xs uppercase tracking-wide font-semibold block mb-2">Add note</label>
      <textarea placeholder="Internal note about this member..." class="w-full bg-white/10 border border-white/15 rounded-xl px-4 py-3 text-white placeholder-white/30 text-sm resize-none h-24"></textarea>
      <button class="mt-2 bg-white/10 text-white/70 text-xs font-semibold px-4 py-2 rounded-full hover:bg-white/20 transition-all">Save note</button>
    </div>`;
  document.getElementById('drawer').classList.remove('hidden');
  document.body.style.overflow='hidden';
}

function closeDrawer() {
  document.getElementById('drawer').classList.add('hidden');
  document.body.style.overflow='';
}

function setStatus(id, status) {
  const m = MEMBERS.find(x=>x.id===id);
  if(m) { m.status=status; renderTable(MEMBERS); closeDrawer(); }
}

function changeStatus(id) { openDrawer(id); }

renderTable(MEMBERS);
</script>
</body>
</html>"""

# Write all files
files = {
    'index.html': LANDING,
    'signup/index.html': SIGNUP,
    'dashboard/index.html': DASHBOARD,
    'admin/index.html': ADMIN_LOGIN,
    'admin/dashboard.html': ADMIN_DASH,
}

for path, content in files.items():
    os.makedirs(os.path.dirname(path) if os.path.dirname(path) else '.', exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Written: {path} ({len(content):,} chars)")

print("\nAll done!")
