## Valkyrie-management-system
**A Command-Line Interface (CLI) Database for Honkai Impact 3rd**
*This project was built entirely from scratch during my first semester to polish my Python fundamentals, algorithmic logic, and data persistence without relying on external frameworks or AI assistance.*

## Overview

The *Valkyrie Management System* is a role-based CLI application designed to manage character data ("Valkyries") for the Schicksal organization. It allows different tiers of users to perform specific administrative tasks, such as recruiting Valkyries, assigning missions, and managing medical status.

The project demonstrates core computer science concepts including *CRUD operations* (Create, Read, Update, Delete), *File I/O* (JSON), and *Authentication logic*.

## Features

# Role-Based Access Control (RBAC)

The system features a dual-login mechanism with distinct permission levels:

  * **Amber (Admin/Manager):**
      * Recruit new Valkyries into the database.
      * Update availability status (e.g., send to Medical, update ERT).
      * View all categories of Valkyries.
  * **Otto (Overseer/Executive):**
      * Assign specific missions to Valkyries.
      * Promote Valkyries to higher ranks.
      * View specialized lists (e.g., by Rank or Mission status).

**Data Persistence**
  * Uses a custom `file_handler.py` module to read and write data to a local `valkyries_database.json` file.
  * Ensures that recruitment, promotions, and mission assignments are saved permanently between sessions.

**Logic & Validation**

  * *Conflict Prevention:* Prevents invalid state changes (e.g., ensures a Valkyrie cannot be assigned a mission if they are already "Injured").
  * *Input Traps:* Includes manual error handling to catch invalid inputs (like entering numbers for names) to prevent database corruption.

**Tech Stack**

  * *Language:* Python 3.x
  * *Database:* JSON (Text-based storage)
  * *Architecture:* Modular Procedural (Separation of Concerns)

## Project Structure

*Valkyrie management system*
*main(vms).py*:Entry point & Authentication logic
*Valkyrie_manager.py*:Module for 'Amber' user logic (CRUD operations)
*Otto.py* :Module for 'Otto' user logic (Promotions/Missions)
*file_handler.py*: Custom utility for JSON reading/writing
*valkyries_database.json* : Persistent storage file
## Future Improvements
* As I continue learning, I plan to implement:
  * *GUI:* Building a frontend using `Tkinter`.
  * *Trying new modules*: Explore new modules that might be useful for the program
