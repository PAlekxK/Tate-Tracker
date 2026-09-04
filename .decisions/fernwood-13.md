## fernwood-13 · onboarding round 1 — nine steps, your pick per step

- project: Tate-Tracker
- loop: tate-tracker
- source: .plans/2026-09-04-independent-queue.md § THE MILESTONE [paul-stated 2026-09-04 ~2:05 PM ET] · the design-options run 2026-09-04 (onboarding) · .plans/2026-09-04-process-wiring-AUDIT.md §D.2
- options: 01-message:A/B/C | 02-arrival:A/B/C | 03-door:A/B/C | 04-name-self:A/B/C | 05-name-place:A/B/C | 06-colour:A/B/C | 07-text-size:A/B/C | 08-icon:A/B/C | 09-first-screen:A/B/C
- exhibit: ~/Desktop/design-options/4-onboarding-round-1.html (staged) · the private Artifact link in the session · source set fernwood-private/.design/2026-09-04-onboarding-mocks/ (exhibits.json = the options as data)
- also-open: the 2026-09-02 door + selector exhibits (staged 9/02, never ruled) sit at the top of the page as baselines

### Why it's here
Paul: *"a robust set of decisions … a lot of those could be made by just walking through some examples of how it could work and then synthesizing the feedback."* Each step shows two or three versions that differ on ONE thing, at 414 × A+ in the app's own design system (a not-yet-live surface — appearance and affordance only; no behaviour is claimed, no her-conditions pass is claimed). The researcher's per-step recommendation and the designer's pick are on the page as data, never as the only option.

### What it means
- **01-message — The message arrives.** The one variable: what the message promises about the end of the flow. **A** The errand · **B** The call-me close (designer's pick) · **C** Names the job
- **02-arrival — The first screen after the tap.** The one variable: how much she gets before she is asked for anything. **A** Bare recognition · **B** What's coming · **C** The place first (designer's pick)
- **03-door — The door — the account.** The one variable: how much of the sign-in she has to handle herself. **A** Shown, not typed (Paul's model) (designer's pick) · **B** One field, nothing else · **C** The conventional login
- **04-name-self — Naming herself.** The one variable: how the optionality of the answer is expressed. **A** Box with a quiet skip · **B** Two real answers (designer's pick) · **C** Ask before the box
- **05-name-place — Naming the place.** The one variable: how the name is offered — default, blank, or default-with-its-consequence-shown. **A** Accept or change (designer's pick) · **B** Blank — she authors it · **C** Shows where it lands
- **06-colour — Personalising — the colour.** The one variable: how much of a choice the colour is. **A** Five swatches, live (designer's pick) · **B** Three named colours · **C** Already chosen
- **07-text-size — Personalising — the text size.** The one variable: whether the size is asked at all, and in what form. **A** The choice · **B** The comfort check · **C** Not asked — the control is shown (designer's pick)
- **08-icon — The home-screen icon.** The one variable: who does the last step — her, or a person on the phone. **A** Teach it · **B** Hand it to a person · **C** Teach it, with a way out (designer's pick)
- **09-first-screen — The first real screen.** The one variable: what greets her when setup ends. **A** No ceremony (designer's pick) · **B** A band naming what she gave · **C** The chooser — two homes

### Recommendation
Walk the page top to bottom on the phone; for each step say the letter, or "none — <what's missing>". Your words land here verbatim (`choice` in decisions.jsonl), a killed option is dropped by its stated reason (`exhibit.py drop`), and the synthesis becomes the onboarding plan's first stage-notes. Three questions only she can answer are in the researcher's Part C — the icon one is thirty seconds on her phone.
