# Frontend DESIGN.md Contract — V1

## Purpose

`DESIGN.md` is the persistent visual-language contract for a frontend project. It records how the product should look and feel so that later frontend work remains consistent.

It is not a substitute for product requirements, UX requirements, technical architecture, or accessibility standards.

## Required sections

```text
# Design System

## Design Direction
## Product Character
## Design Dials
## Typography
## Color
## Spacing
## Layout
## Components
## Navigation
## Forms
## Feedback / States
## Motion
## Responsive Behavior
## Accessibility
## Anti-Patterns
```

## Design Direction

State the visual direction in concrete terms:

- composition
- hierarchy
- density
- tone
- visual contrast
- use of imagery
- interaction character

Avoid vague statements such as "modern and beautiful" without operational meaning.

## Design Dials

When useful, record qualitative or numeric guidance for:

- `DESIGN_VARIANCE`: conservative to experimental layout
- `MOTION_INTENSITY`: static to highly animated
- `VISUAL_DENSITY`: spacious to information-dense

These are guidance values, not universal defaults.

## Typography

Specify:

- primary font
- secondary/display font if applicable
- body scale
- heading hierarchy
- line heights
- weight usage
- text wrapping expectations

## Color

Specify semantic tokens rather than scattered one-off colors where practical:

- background
- surface
- elevated surface
- text
- muted text
- border
- primary action
- secondary action
- success
- warning
- error
- focus

Include contrast expectations.

## Spacing and layout

Specify the spacing rhythm, container behavior, grid/flex rules, maximum widths, alignment principles, and major responsive transitions.

## Components

Record reusable patterns and variants for components that materially define the product language.

## States

Define expected visual treatment for:

- loading
- empty
- error
- success
- disabled
- hover
- focus
- selected/active

## Motion

Document where motion is appropriate, what it communicates, duration/easing guidance, and where reduced-motion behavior is required.

Motion must reinforce interaction rather than decorate every element.

## Responsive behavior

Describe behavior at representative viewport classes. Do not rely only on breakpoint numbers; state what changes in hierarchy, navigation, density, and interaction.

## Accessibility

Record product-specific accessibility expectations including contrast, keyboard focus, semantic controls, touch targets, reduced motion, and readable text sizing.

## Anti-Patterns

Explicitly record patterns that should not appear in this product, such as:

- inconsistent button styles
- arbitrary spacing values
- decorative animation with no purpose
- inaccessible custom controls
- duplicated component variants
- placeholder content in shipped flows
- generic hero sections where the product does not need them

## Change control

A material change to `DESIGN.md` can affect existing screens. The worker should identify impacted screens and re-run appropriate visual/regression checks before declaring completion.
