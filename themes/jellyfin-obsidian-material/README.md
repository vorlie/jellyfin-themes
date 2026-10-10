# Jellyfin Obsidian Material / Material 3 Design System

A desktop-first visual redesign for Jellyfin Web built around a dark obsidian palette, restrained glass surfaces, and a Material 3-inspired interface.

## Compatibility

| Theme Version | Jellyfin Target | Status |
| :--- | :--- | :--- |
| `v12.1.x` | Jellyfin 12.1.x | Active |

---

## Architecture & File Structure

The redesign is modularized into layered CSS files that keep the visual system organized and easy to maintain.

| File | Surface / Purpose |
| :--- | :--- |
| [`01-tokens.css`](./01-tokens.css) | Central design tokens for surfaces, borders, text, accents, spacing, and glass optics. |
| [`02-shell.css`](./02-shell.css) | Global canvas background, backdrop darkening, typography, scrollbars, focus rings, and motion handling. |
| [`03-header.css`](./03-header.css) | Header chrome, nav shell, action buttons, search UI, and user controls. |
| [`04-cards.css`](./04-cards.css) | Media cards, hover states, overlay badges, progress indicators, and metadata styling. |
| [`05-details.css`](./05-details.css) | Details and metadata layouts, posters, ribbons, and media content presentation. |
| [`06-playback.css`](./06-playback.css) | Playback controls, OSD chrome, sliders, volume controls, and subtitle-safe treatment. |
| [`07-upnext.css`](./07-upnext.css) | Up Next panels, countdown states, and action focus styling. |
| [`08-dialogs.css`](./08-dialogs.css) | Dialogs, action sheets, popovers, filter UI, and notifications. |
| [`09-forms-and-dashboard.css`](./09-forms-and-dashboard.css) | Input styles, tables, card lists, and dashboard configuration surfaces. |
| [`10-tweaks.css`](./10-tweaks.css) | Final polish, compatibility adjustments, and edge-case tuning. |
| [`theme.css`](./theme.css) | Entry point that imports the modular layer files. |
| [`bundle.min.css`](./bundle.min.css) | Production-ready bundled stylesheet for direct use in Jellyfin. |

---

## Design Principles & Implementation Safeguards

1. **Dark Obsidian Palette**:
   - The theme uses a deep black/charcoal canvas with refined violet accents and subdued glass translucency.
   - It preserves readability while keeping a premium, low-glare presentation.

2. **Glass-Inspired Surfaces**:
   - `backdrop-filter` is used selectively so floating panels feel elevated without hurting performance or subtitle readability.
   - Large content areas remain stable and legible for smooth scrolling.

3. **Playback Subtitle Safety**:
   - OSD and overlay UI avoid heavy opaque blocks that could obscure video subtitles.

4. **TV-Safe and Accessible**:
   - `.layout-tv` adjustments reduce expensive effects for television layouts.
   - Focus and interaction states remain clearly visible and keyboard-friendly.

---

## How to Apply

### Method 1: Jellyfin Server Dashboard (Recommended)
1. Open your Jellyfin Web instance and sign in as an administrator.
2. Go to **Dashboard** &rarr; **General**.
3. Scroll down to the **Custom CSS code** section.
4. Copy the contents of [`bundle.min.css`](./bundle.min.css) and paste it into the textarea.
5. Click **Save**.

### Method 2: Modular Development
Use [`theme.css`](./theme.css) in a browser or local web host during development.

### Method 3: Local Preview with Python
Preview the theme locally from this folder using Python:

```bash
cd /path/to/jellyfin-themes/themes/jellyfin-obsidian-material
python3 -m http.server 8787 --bind 0.0.0.0 --directory .
```

On Windows:

```powershell
cd .\jellyfin-themes\themes\jellyfin-obsidian-material
py -m http.server 8787 --bind 0.0.0.0 --directory .
```

Then open:

```text
http://localhost:8787/
```

This is useful for testing the design before copying the final bundled CSS into Jellyfin.

If you want to keep making personal tweaks on top of the local theme while your Jellyfin instance loads it live, add an import in your custom CSS such as:

```css
@import url("http://192.168.0.27:8787/theme.css");
```

or, for the bundled production variant:

```css
@import url("http://192.168.0.27:8787/bundle.min.css");
```

This lets you iterate on the theme quickly without copying the CSS back into Jellyfin each time.

### Method 4: Build the Release Bundle
From this theme folder, run:

```bash
npx esbuild theme.css --bundle --minify --outfile=bundle.min.css
```

This generates the production-ready CSS bundle used in Jellyfin's Custom CSS field.

---

## Notes

This theme is written for Jellyfin Web and is intended to be applied as custom CSS. It is designed for a modern desktop-first UI and remains compatible with the 12.1 series target.
