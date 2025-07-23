# 🧹 Messy Migration - Retainsure Challenge (Refactored)

This project is a solution to the Retainsure Software Engineering assignment — focused on **cleaning, transforming, and migrating messy user data** from a poorly structured SQLite database table to a clean, normalized table.

---

---

## 🧠 Problem Statement

- You are given a `usres` table with incorrect column names, inconsistent casing, extra whitespace, and improperly formatted phone numbers/emails.
- The goal is to clean and migrate this data into a well-structured `users` table with correct formatting and validation.

---

## ✅ Features

- Extracts messy data from legacy SQLite `usres` table.
- Cleans and normalizes:
  - **First and last names**
  - **Email addresses** (lowercased + trimmed)
  - **Phone numbers** (standardized to `+91-XXXXXXXXXX`)
- Creates a clean `users` table with proper schema.
- Handles duplicates and invalid entries gracefully.
- Modular code organized into `models`, `routes`, and `utils`.

---

## 🚀 Usage

### 1. Migrate & Clean Data

```bash
python refactored/migrate_data.py
```
### 2. View Cleaned Users
```bash
python refactored/view_users.py

