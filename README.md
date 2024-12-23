# Simple-API (QR-API)

This repository serves as a foundational example of using Flask along with gunicorn to create a web server REST API.
This codebase was developed and used for a scavenger hunt among friends in 2024 whereby a number of QR codes, printed,
were placed around the house.

## Scavenger Hunt Gameplay
QR codes are printed on pieces of paper and hidden around the "game area" for the group to find. For each QR code found by a user,
the user will scan the code, which will take them to an item description page. The items represent "power-ups" that the user
can employ on other players throughout the game. The user can claim the item by adding it to their inventory on this item
description page. Each item can only be claimed once per game. When a user is ready to use an item, they will publicly declare
it and must show that they are pressing the "Use Item" button in the UI. The game Admin can view who owns what items and
ensure that if an item is being used, the user has in fact relinquished the item from their inventory.

## Results
During the only formal use of the API in 2024, it performed without any major bugs. User items were properly tracked, access
to endpoints was appropriately restricted, and the gameplay was fairly seamless for users. Feedback for improvements included:
- UI reacting to user input more clearly (e.g., providing a confirmation message that an item was successfully 
added to the inventory without the user needing to navigate to their inventory to confirm).
- A more mobile-friendly UI (proper scaling and sizing of elements on mobile browsers). Though designed with mobile in mind,
much improvement could be made here.
- Safari support (Safari privacy around cookies made the app unusable on Safari for certain players)

Overall, the app successfully performed to its intended use on its one and only public deployment.

## Deployment
During the public deployment, the API was accessible on the public Internet using the
[Digital Ocean App Platform](https://www.digitalocean.com/products/app-platform) offering. App Platform allows for a super simple
deployment process whereby you can deploy a Docker container directly using the source code repository (or, a container image
directly from an online registry). In this case, Simple-API had this repo linked and App Platform could simply deploy it using
the Dockerfile.

Note: when testing multiple users on the initial deployment to App Platform, it was observed that user profiles were being
"mixed" (i.e., users were seeing each other's profiles at random every time a page was loaded). This was due to the App Platform
replicas being set to 2 - thus there were two separate SQLite databases being used and user IDs were being retrieved based
on which replica handled the request. Because the simplicity of the app lends itself well to SQLite and Digital Ocean only provides
persistent storage in the form of PostgreSQL for App Platform, the simple solution in this case was to reduce the replicas to 1.
This resolved the issue, though, if Simple-API were to be deployed long-term, a persistent database would become an immediate
requirement.

## Notable Features
- Admin Access (allowing an admin user(s) to view the progress of the game and reset certain actions)
- Username/password authentication enforced through redirects
- Browser sessions, allowing for seamless gameplay when a user frequently revisits the page
- Sound gameplay mechanics enforced by design
- Helper code to manage Flask db-init and seed the database with item data from `item_info` module