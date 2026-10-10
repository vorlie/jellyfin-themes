# Jellyfin Web Liquid Glass / Material 3 Redesign

A desktop-first visual redesign for Jellyfin Web crafted in pure modern CSS/SCSS with a **Liquid Glass / Material 3-inspired aesthetic**.

---

## Architecture & File Structure

The redesign is modularized into nine distinct layers, each targeting specific architectural components without relying on volatile generated hash classes:

| File | Surface / Purpose |
| :--- | :--- |
| [`01-tokens.css`](./01-tokens.css) | Centralized CSS custom properties: surfaces, borders, text, accents, geometry, elevations, and glass optics. |
| [`02-shell.css`](./02-shell.css) | Global canvas background, backdrop darkening, typography, floating scrollbars, focus rings, and reduced motion. |
| [`03-header.css`](./03-header.css) | Liquid-glass header island, pill navigation tabs, action buttons, search, and user avatar. |
| [`04-cards.css`](./04-cards.css) | Unified media cards, restrained hover lift, image scale, overlay action discs, progress bar, and badges. |
| [`05-details.css`](./05-details.css) | Media details page: soft backdrop gradient, elevated poster, glass action ribbon, and metadata chips. |
| [`06-playback.css`](./06-playback.css) | Video playback OSD: non-intrusive gradient controls, glowing slider, volume pills, and subtitle-safe layers. |
| [`07-upnext.css`](./07-upnext.css) | Elevated liquid-glass Up Next card, countdown emphasis, and action buttons. |
| [`08-dialogs.css`](./08-dialogs.css) | Modal dialogs, action sheets, popover menus, filter dialog, and floating toast notifications. |
| [`09-forms-and-dashboard.css`](./09-forms-and-dashboard.css) | Inputs, textareas, dropdowns, checkboxes, paper lists, settings cards, and dashboard tables. |
| [`theme.css`](./theme.css) | Master development entry point importing all 9 modular files via `@import`. |
| [`bundle.min.css`](./bundle.min.css) | Standalone minified concatenated release stylesheet (`npx esbuild theme.css --bundle --minify --outfile=bundle.min.css`). |

---

## Design Principles & Implementation Safeguards

1. **Restrained Liquid Glass**:
   - `backdrop-filter: blur(...) saturate(...)` is applied selectively to floating navigation surfaces, dialogs, action sheets, and Up Next cards.
   - Large scrolling containers and repeated card grids remain stable opaque/subtle surfaces for 60fps scrolling performance.

2. **Playback Subtitle Protection**:
   - Video OSD uses soft alpha gradients rather than solid block panels to prevent obscuring ASS subtitles or SubtitlesOctopus worker rendering.

3. **TV Compatibility Protected**:
   - Every module includes `.layout-tv` guards that turn off expensive blur filters and restore solid backgrounds and D-pad spatial focus indicators.

4. **Accessibility First**:
   - Includes `@media (prefers-reduced-motion: reduce)` rules.
   - Focus rings use `:focus-visible` and Jellyfin's `.show-focus` states for high-contrast keyboard navigation.

---

## How to Apply

### Method 1: Jellyfin Server Dashboard (Recommended)
1. Open your Jellyfin Web instance and sign in as an administrator.
2. Go to **Dashboard** &rarr; **General**.
3. Scroll down to the **Custom CSS code** section.
4. Copy the entire contents of [`bundle.min.css`](./bundle.min.css) and paste it into the textarea.
5. Click **Save**.

### Method 2: Modular Development
Link [`theme.css`](./theme.css) inside your web host or development environment.
