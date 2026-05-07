# Getting Started with Cowork

This folder contains your Cowork setup for automating and accelerating your apparel import business.

## What is Cowork?

Cowork is an AI automation tool that runs tasks with access to your real tools (email, calendar, Slack, web, etc.). You trigger it by typing a `/` command or describing what you need, and it handles multi-step workflows using **Skills** (reusable automation templates) and **Plugins** (bundles of skills for specific domains).

**For your business:** automate buyer comms, monitor competitors in real-time, manage vendor workflows, and maintain institutional knowledge about buyers and suppliers.

---

## Quick Start (5 minutes)

### Step 1: Install Plugins
Open Cowork and follow these steps:

1. Click **Manage Plugins** (or `/setup` if available)
2. Search for and add these three plugins:
   - **Nimble** — Competitive intelligence and market research
   - **Operations** — Vendor and process management  
   - **Productivity** — Task management and memory

See `COWORK_SETUP.md` for full details on each plugin.

### Step 2: Connect Your Tools
Once plugins are installed, you'll need to authenticate them to your accounts:

1. **Gmail** — For buyer/vendor email access
2. **Google Calendar** — For deadlines and meetings
3. **Slack** — For team updates
4. **Notion** — For vendor database and notes
5. **Nimble MCP Server** — For web search and competitive data

Go to **Settings → Connectors** and click each one to authenticate. It takes ~2 minutes per tool.

### Step 3: Try Your First Skill
Pick one of these to get started:

**If you want competitive intelligence:**
- Type `/nimble:competitor-intel` or describe: "Give me a competitive brief on Primark's latest moves in the $20-40 dress category"

**If you want to organize vendors:**
- Type `/operations:vendor-review` or describe: "Evaluate my top 5 apparel suppliers and score them on quality, lead time, and price"

**If you want to build memory:**
- Type `/productivity:memory-management` or describe: "I need to remember key details about my top 10 buyers — preferences, seasonal patterns, lead times"

---

## Next Steps (Week 1)

- [ ] Install all three plugins
- [ ] Connect Gmail, Google Calendar, Slack, Notion
- [ ] Run your first competitive intelligence report
- [ ] Set up your buyer memory (key accounts and their preferences)
- [ ] Document one workflow (sourcing process or order cycle)

See the **First 30 Days** section in `COWORK_SETUP.md` for more quick wins.

---

## Commands You'll Use

Once plugins are installed, type `/` in Cowork to see available commands. Key ones for your business:

**Competitive Intelligence:**
- `/nimble:competitor-intel` — Track competitor moves, pricing, launches
- `/nimble:competitor-positioning` — Monitor how retailers position themselves
- `/nimble:market-finder` — Discover retail buyers and market opportunities

**Vendor & Process:**
- `/operations:vendor-review` — Evaluate and negotiate with suppliers
- `/operations:process-doc` — Document sourcing or order workflows
- `/operations:process-optimization` — Identify bottlenecks and speed things up

**Memory & Tasks:**
- `/productivity:memory-management` — Build and maintain buyer/vendor context
- `/productivity:task-management` — Track sourcing deadlines and buyer requests

---

## How It Works

1. **You describe what you need** — "Monitor Zara's pricing on summer dresses" or "Create a vendor scorecard"
2. **Cowork picks the right skill** — Matches your request to the right plugin
3. **The skill runs autonomously** — Pulls data from your tools, formats it, delivers results
4. **You iterate** — Ask follow-up questions, refine, save results

---

## Troubleshooting

**"I don't see the `/` commands"**
- Restart Cowork or refresh the sidebar
- Make sure all plugins are fully installed (check green checkmarks)

**"A skill says it needs a connector I haven't connected"**
- Go to **Settings → Connectors** and authenticate that tool
- Most connectors use OAuth (click "Connect" and approve in your browser)

**"I want to add another plugin later"**
- Anytime—no need to restart. Go to **Manage Plugins** and add more

**"I'm getting confused by all the skills"**
- Start with just one plugin (Nimble for competitive intel, or Productivity for memory)
- Add others once you're comfortable

---

## Important Files

- **COWORK_SETUP.md** — Full context: why each plugin matters, which connectors you need, and use cases
- **README.md** (this file) — Quick start and troubleshooting
- Your Cowork session will create **CLAUDE.md** and a **memory/** directory for storing context about buyers, vendors, and market data

---

## Support & Learning

- **Stuck on a skill?** Describe what you're trying to do in plain language—Cowork will guide you
- **Want to know more?** Open `COWORK_SETUP.md` for detailed plugin descriptions and strategies
- **Need to onboard someone else?** Share this folder (`README.md` + `COWORK_SETUP.md`) and have them follow the Quick Start steps above

---

**Ready?** Open Cowork, go to Manage Plugins, and install Nimble first. Then come back and run a competitive intelligence report.
