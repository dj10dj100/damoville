# Cowork Setup Configuration

**Date Created:** May 7, 2026  
**For:** B2B Fashion Import Business (Apparel Wholesale)

## Business Context

Running a clothing import operation that supplies high-street and FMCG retailers (Primark, Zara, etc.). Core focus:
- Global supply chain and sourcing efficiency
- Buyer relationship management and communications
- Fast-moving retail trend awareness and competitive intelligence

## Strategic Goals

1. **Automate the trivial** — Free up time from repetitive admin, comms, and reporting
2. **Build competitive intelligence** — Track competitor moves, retail pricing trends, and emerging product categories
3. **Improve business efficiency** — Tighten workflows across sourcing, buyer communications, order management, and analysis

---

## Plugins to Install

### 1. **Nimble** (`nimble@knowledge-work-plugins`)
**Purpose:** Live web data for competitive intelligence and market research

**Key Skills:**
- `nimble:competitor-intel` — Track competitor moves, pricing changes, product launches
- `nimble:competitor-positioning` — Monitor how competitors and retailers position themselves online
- `nimble:market-finder` — Discover and audit retail buyer accounts, market segments, and TAM
- `nimble:company-deep-dive` — Research retail chains, their strategies, positioning, and financial context

**Connectors Required:**
- `nimble-mcp-server` (Live web search, scraping, and structured data extraction)

**Use Cases:**
- Weekly competitive pricing monitoring on key product categories
- Track what Primark, Zara, H&M are doing (new lines, positioning shifts)
- Discover new retail buyers and market opportunities
- Research supplier pricing trends and alternatives

---

### 2. **Operations** (`operations@knowledge-work-plugins`)
**Purpose:** Vendor and process management

**Key Skills:**
- `operations:vendor-review` — Evaluate suppliers, negotiate terms, assess vendor risk
- `operations:process-doc` — Document sourcing, order fulfillment, buyer communication workflows
- `operations:process-optimization` — Identify bottlenecks and streamline cycles
- `operations:risk-assessment` — Assess supply chain, regulatory, and vendor risks

**Connectors Required:**
- `slack` — Team communication
- `google calendar` — Schedule and deadlines
- `gmail` — Vendor and buyer emails
- `notion` — Vendor information, contracts, notes
- `ms365` — Shared vendor/order tracking documents (optional)

**Use Cases:**
- Evaluate new suppliers vs. incumbent vendors
- Document standardized order and fulfillment processes
- Analyze cycle time in sourcing and order management
- Risk assessment on key vendor relationships

---

### 3. **Productivity** (`productivity@knowledge-work-plugins`)
**Purpose:** Task automation and institutional memory

**Key Skills:**
- `productivity:memory-management` — Build and maintain context on buyers, vendors, market dynamics, team shorthand
- `productivity:task-management` — Track buyer requests, orders, follow-ups, sourcing deadlines
- `productivity:update` — Sync tasks from email, calendar, and project trackers into one system

**Connectors Required:**
- `slack` — Team messages and updates
- `gmail` — Email-sourced tasks and buyer requests
- `google calendar` — Meetings and deadlines
- `notion` — Shared knowledge base
- `asana` / `linear` / `monday` / `clickup` (pick one or more if you use them) — Project tracking

**Use Cases:**
- Remember buyer preferences, seasonal patterns, and relationship context
- Auto-surface vendor follow-ups and order deadlines
- Track internal team context and project status
- Build searchable knowledge base of past buyer interactions and commitments

---

## Recommended Connectors to Connect

### Immediate (Day 1)
- **Gmail** — Core channel for buyer and vendor communications
- **Google Calendar** — Deadlines, buyer meetings, seasonal cycles
- **Slack** — Team coordination and updates
- **Notion** — Vendor database, buyer notes, sourcing templates

### Soon (Week 1)
- **Nimble MCP Server** — Enable competitive intelligence workflows
- **Atlassian** (Jira/Confluence) OR **Asana** OR **Monday.com** — If you use one for order/project tracking

### As Needed
- **MS365** — If using Excel for shared vendor/order tracking
- **Docusign** — For vendor contract workflow (if using with Legal plugin later)

---

## Setup Checklist

- [ ] Install Nimble plugin
- [ ] Install Operations plugin  
- [ ] Install Productivity plugin
- [ ] Connect Gmail
- [ ] Connect Google Calendar
- [ ] Connect Slack
- [ ] Connect Notion
- [ ] Set up memory system (CLAUDE.md + memory/ directory for buyer/vendor/market context)
- [ ] Create first task list (TASKS.md) — buyer projects, sourcing deadlines, competitive monitoring
- [ ] Run first competitor intelligence report
- [ ] Document a key workflow (sourcing process, order cycle, buyer comms)

---

## First 30 Days — Quick Wins

1. **Week 1:** Set up productivity memory for 5-10 key buyers and top 5 vendors
2. **Week 1:** Run a competitive intelligence briefing on 3 key competitors/retailers
3. **Week 2:** Document and time the sourcing-to-order cycle end-to-end
4. **Week 2:** Create vendor evaluation template for next supplier review
5. **Week 3:** Set up automated weekly competitive pricing monitoring on key categories
6. **Week 4:** Build buyer preference summary (seasonal, quality, price bands, lead times)

---

## Questions?

- **Nimble not finding competitors you care about?** Use `/nimble:company-deep-dive` for specific retailer research first
- **Too many tasks?** Start with Productivity plugin's memory system—context matters more than tool count
- **Vendor data scattered?** Operations' vendor-review skill can help audit what's where
- **Want to add more?** Legal plugin (contract review) and Brightdata (web scraping) are good later additions

---

**Last Updated:** May 7, 2026  
**Created by:** Daniel Jenkins (dan@daniel-jenkins.com)
