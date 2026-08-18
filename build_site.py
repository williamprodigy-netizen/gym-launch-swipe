#!/usr/bin/env python3
"""Build the PB Trading swipe site. Run: python3 build_site.py"""
import sys, os, glob, subprocess
sys.path.insert(0, os.path.expanduser("~/scripts/_swipe_builder"))
from swipebuild import build

REPO = os.path.dirname(os.path.abspath(__file__))
PKG = os.path.expanduser("~/Downloads/Swipes/GYM_LAUNCH_Swipe")


def _probe(p):
    try:
        return int(float(subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "csv=p=0", p], capture_output=True, text=True, timeout=60).stdout.strip()))
    except Exception:
        return 0


def video_library():
    rows = []
    for p in sorted(glob.glob(os.path.join(PKG, "Recording/**/*.mp4"), recursive=True)):
        mb = os.path.getsize(p) / 1e6
        rows.append((os.path.basename(p), _probe(p),
                     f"{mb/1000:.1f} GB" if mb >= 1000 else f"{mb:.0f} MB",
                     ROLES.get(os.path.basename(p), "")))
    return rows


ROLES = {}

CONFIG = {
 "SITE": "Gym Launch — 2026 Growth Playbook",
 "CREATOR": "Alex Hormozi",
 "ADS_KEY": "gym_launch",
 "FUNNEL_IDS": ["F035"],
 "CAPTURED": "18 August 2026",
 "REPO": REPO,
 "PACKAGE": "~/Downloads/Swipes/GYM_LAUNCH_Swipe",
 "BLURB": "Their ads do <b>not</b> point at gymlaunch.com. All 94 of them point at a separate "
          "squeeze page on <code>scale.gymlaunch.com</code> giving away a 137-page playbook.",
 "PAGES": [("index.html","Overview"),("analysis.html","Analysis"),
              ("transcripts.html","Transcripts"),("videos.html","Video library")],
 "STATS": [("Active ads","<b>68</b>"),("Ads at the playbook","94"),
           ("Distinct concepts","<b>3</b>"),("Top score","96 / Winning"),
           ("FB page id","236192553431770"),("Lead magnet","137-page PDF"),
           ("Scale claim","6,000+ gym owners"),("Price","never stated")],
 "OFFER": [("Product","Done-for-you gym growth &mdash; coaching plus systems"),
   ("Paid lead magnet","<b>2026 Gym Growth Playbook</b> &mdash; &ldquo;why your gym is stuck, and the blueprint to get it growing again&rdquo;"),
   ("Who it targets","&ldquo;Gym owners who are doing <b>&lsquo;ok&rsquo; on paper</b>, but haven't seen a real jump in members, revenue, or profit in a long time&rdquo;"),
   ("Organic front door","A <b>free Skool group</b> &mdash; &ldquo;the #1 gym growth community&rdquo;"),
   ("Claim","&ldquo;Gym Launch helps build a new <b>7-figure gym every 21 days</b>&rdquo;"),
   ("Path","Paid ad &rarr; squeeze &rarr; HubSpot &rarr; nurture &rarr; /contact &ldquo;qualify for a quick call&rdquo; &rarr; call"),
   ("Price","<b>Never stated</b> on any captured page")],
 "FINDINGS": [
  ("Their ads never touch the main site &mdash; third competitor in this file doing this",
   "All <b>94</b> playbook ads point at <code>scale.gymlaunch.com/playbook</code>. The main site "
   "<code>gymlaunch.com</code> carries only GTM and HubSpot &mdash; <b>no Meta Pixel at all</b>. The "
   "squeeze page carries Meta Pixel, Clarity, HubSpot, Intercom, ClickFunnels and New Relic. Two "
   "entirely different stacks. <b>Viral Coach and Brez Scales do the same thing.</b> Three unrelated "
   "operators separate the brand site from the paid conversion page; we run one page for both jobs."),
  ("94 ads, 3 ideas",
   "Collapsed by copy, the 94 records are only <b>three concepts</b> &mdash; and the spread is "
   "lopsided: 28 variants of the winner, 11 of the one still testing, 1 of the third. That is "
   "Andromeda bundling in the open. <b>They are not writing new ads, they are re-uploading the one "
   "that works.</b> The winning concept is a <b>9-second video</b>."),
  ("The subhead disqualifies the desperate on purpose",
   "&ldquo;For gym owners who are doing <b>&lsquo;ok&rsquo; on paper</b>, but haven't seen a real "
   "jump in&hellip; a long time.&rdquo; It does not target the gym about to close. It targets the "
   "plateaued owner who still has money and has stopped believing anything will change. That is a "
   "buyer, not a charity case. <span class=\"tag good\">worth stealing</span>"),
  ("The best hook is a fragility argument, not a promise",
   "&ldquo;If your gym only has one way to get new members, <b>you're one bad month away from a real "
   "problem</b>.&rdquo; Scored <b>96 / Winning</b> with 28 variants. It sells nothing and promises "
   "nothing &mdash; it just makes the prospect's current stability feel like luck."),
  ("They cannot keep their own page count straight",
   "The same PDF is advertised as <b>&ldquo;130 plus pages&rdquo;</b>, <b>&ldquo;140+ pages&rdquo;</b> "
   "and <b>&ldquo;137 pages&rdquo;</b> across three live concepts. Recorded as observed. Either "
   "sloppy, or evidence that the number itself is being tested."),
  ("The brand is stale in our own registry",
   "The best-performing ad is signed <b>&ldquo;Mike&rdquo;</b>, not Alex Hormozi. Hormozi sold Gym "
   "Launch; our registry still lists him as the creator. Flagged rather than silently corrected."),
 ],
 "FUNNEL": [
  ("PAID squeeze","scale.gymlaunch.com/playbook",'<span class="tag good">where every ad lands</span> Free 137-page playbook. HubSpot form. <b>Meta Pixel + Clarity + Intercom + ClickFunnels + New Relic.</b>'),
  ("Main page","gymlaunch.com","&ldquo;Do you want more members?&rdquo; Free Skool group. <b>GTM + HubSpot only, no Meta Pixel.</b>"),
  ("Apply","gymlaunch.com/contact","&ldquo;Your gym should be full. Your bank account should be too.&rdquo; &ldquo;Qualify for a quick call.&rdquo;"),
  ("Client wins","/gym-types/client-wins","Screenshotted internal wins with hashtags &mdash; #FastCash, #Helpingisourgoal."),
  ("Case studies","/gym-types/case-studies","Named gyms: Raw Fitness, L&amp;D Fitness, Map Training."),
  ("Stories","/gym-types/stories","&ldquo;We signed up 26 people in the first WEEK.&rdquo;"),
 ],
 "TRANSCRIPT_GROUPS": [],
 "SLIDE_PAGES": [],
 "ANALYSIS": """
<div class="note"><b>The finding is where the ads go.</b> Will assumed the funnel was gymlaunch.com.
It is not. Every one of their 94 playbook ads lands on <code>scale.gymlaunch.com/playbook</code>, a
page with a completely different tech stack. The main site is brand; the subdomain is the machine.</div>

<h2 class="sec">Two sites, two stacks</h2>
<div class="tablewrap"><table>
<tr><th>Page</th><th>Trackers</th><th>Job</th></tr>
<tr><td>gymlaunch.com</td><td>GTM, HubSpot</td><td>Brand, organic, Skool group</td></tr>
<tr><td><b>scale.gymlaunch.com/playbook</b></td><td><b>Meta Pixel</b>, Clarity, HubSpot, Intercom, ClickFunnels, New Relic</td><td><b>Convert cold paid traffic</b></td></tr>
<tr><td>gymlaunch.com/contact</td><td>GTM, HubSpot</td><td>Application / qualify for a call</td></tr>
</table></div>
<p style="margin-top:12px"><span class="tag">READ</span> Three unrelated competitors in this swipe
file &mdash; Gym Launch, Viral Coach, Brez Scales &mdash; all split the brand site from the paid
conversion page. <b>Our class registration page is asked to be both at once.</b></p>

<h2 class="sec">The three concepts, ranked</h2>
<div class="tablewrap"><table>
<tr><th>Concept</th><th>Variants</th><th>Score</th><th>Length</th></tr>
<tr><td><b>&ldquo;One channel &rarr; one bad month away from a real problem&rdquo;</b></td><td><b>28</b></td><td><b>96 Winning</b></td><td>9s</td></tr>
<tr><td>&ldquo;OFFICIAL ANNOUNCEMENT &mdash; the playbook just dropped&rdquo;</td><td>11</td><td>1 Testing</td><td>87s</td></tr>
<tr><td>&ldquo;This is a Gift&hellip;&rdquo; &mdash; signed by Mike</td><td>1</td><td>96 Winning</td><td>74s</td></tr>
</table></div>
<p style="margin-top:12px">The 9-second winner carries 28 variants; the 87-second announcement is
still at score 1. <b>Short and fragility-framed is beating long and announcement-framed</b>, on their
own money. Small n, one snapshot, but the variant counts show where they are putting budget.</p>

<h2 class="sec">Why the playbook offer is strong</h2>
<p>It is not &ldquo;a free guide&rdquo;. It is <b>137 pages</b>, and the ad copy names the chapters
&mdash; offers, traffic, nurture, sales, month-1 money model &mdash; along with the concepts inside
(CAC, LTV), and then adds <i>&ldquo;if you're not sure what CAC or LTV is, I cover it in the first
section.&rdquo;</i> That single parenthetical admits the reader might not know, without insulting
them, and widens the audience to owners who would otherwise self-disqualify.</p>
<p><span class="tag">EVIDENCE</span> &ldquo;Over 6,000 gym owners downloaded our last playbook&rdquo;
&mdash; they use last year's download count as proof for this year's asset.</p>

<h2 class="sec">What is missing</h2>
<ul><li><b>The playbook PDF itself.</b> Requires submitting the HubSpot form &mdash; needs Will's
approval, since that is a real opt-in.</li>
<li><b>The nurture sequence</b> that follows the download. Same blocker.</li>
<li><b>No price</b> anywhere in the captured funnel.</li>
<li><b>The 3 ad videos are identified with signed download URLs but not pulled locally.</b></li></ul>
""",
}
CONFIG['VIDEOS'] = video_library()

if __name__ == '__main__':
    build(CONFIG)
