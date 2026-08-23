sidhivinayaksoftwork — IT Company Website TODO

Official Website Name

sidhivinayaksoftwork

This is the official company/website name and should be used consistently across the project, including branding, page titles, metadata, documentation, and deployment configuration where applicable.

Project Overview

Build a modern, premium, full-stack IT company website inspired by:

Ravwolf

Infybright

Softude

The website must be original and must NOT directly copy their layouts, text, branding, images, or source code.

Technology Stack

Frontend

React

Vite

React Router

Tailwind CSS

Framer Motion

Axios

Lucide React

Backend

Django

Django REST Framework

PostgreSQL

JWT authentication where required

Django Admin

Deployment

Frontend: Vercel

Backend: Render

Database: Render PostgreSQL

Production API served by Django/Gunicorn on Render

Environment variables managed separately on Vercel and Render

CORS configured for the Vercel frontend domain

Phase 1 — Project Setup

Repository

Create project root

Create frontend/

Create backend/

Create .gitignore

Create .env.example

Create README.md

Create TODO.md

Create AGENT.md

Django

Create Django project

Configure Django REST Framework

Configure PostgreSQL

Configure CORS

Configure environment variables

Configure static files

Configure media files

Configure Django Admin

Configure API versioning

Configure production settings

Configure Gunicorn

React

Create Vite React application

Configure Tailwind CSS

Configure React Router

Configure Axios

Configure Framer Motion

Create global design system

Create reusable UI components

Configure production API URL using environment variables

Phase 2 — Design System

Brand

Define company name

Define logo

Define primary color

Define secondary color

Define accent color

Define typography

Define spacing system

Define border radius

Define shadows

Define animations

UI Components

Navbar

Mobile navigation

Footer

Button

Badge

Card

Section heading

Container

Input

Textarea

Select

Modal

Loading state

Empty state

Error state

Toast notification

Pagination

Breadcrumbs

Phase 3 — Homepage

Hero

Create premium hero section

Add headline

Add supporting text

Add primary CTA

Add secondary CTA

Add animated visual

Add subtle background effects

Make hero responsive

Trust Section

Add client/partner logos

Add trust statement

Add statistics

Services Preview

Web Development

Mobile App Development

AI & Machine Learning

UI/UX Design

Cloud & DevOps

Software Development

ERP/CRM

IT Consulting

Featured Work

Create featured project section

Add project cards

Add project categories

Add technology badges

Add project detail links

Why Choose Us

Add company advantages

Add development methodology

Add statistics

Technology Section

Frontend technologies

Backend technologies

Mobile technologies

Database technologies

Cloud technologies

AI technologies

Industries

Healthcare

FinTech

Education

E-Commerce

Real Estate

Logistics

SaaS

Manufacturing

Process

Discovery

Strategy

UI/UX

Development

Testing

Deployment

Maintenance

Testimonials

Create testimonial carousel

Add client name

Add company

Add designation

Add testimonial

Blog Preview

Latest articles

Categories

Featured article

Final CTA

Create strong CTA section

Add contact button

Add project inquiry CTA

Phase 4 — About Page

Company introduction

Company story

Mission

Vision

Core values

Company statistics

Team section

Development philosophy

CTA

Phase 5 — Services

Services Page

Service listing

Service categories

Service descriptions

Service icons

CTA

Service Detail

Create dynamic service pages.

Overview

Benefits

Features

Technologies

Development process

FAQ

Related projects

CTA

Phase 6 — Portfolio

Portfolio listing

Category filtering

Technology filtering

Search

Pagination

Project cards

Project Detail

Project overview

Client

Industry

Challenge

Solution

Features

Technologies

Results

Screenshots

Related projects

CTA

Phase 7 — Case Studies

Case study listing

Featured case study

Case study detail

Client information

Problem

Strategy

Implementation

Technology

Results

Metrics

Images

CTA

Phase 8 — Technologies

Create technology categories.

Frontend

Backend

Mobile

Database

Cloud

DevOps

AI/ML

CMS

Testing

Each technology should have:

Name

Logo

Description

Category

Website URL

Display order

Phase 9 — Blog

Backend

Blog model

Category model

Tag model

Author model

SEO fields

Featured image

Published date

Draft/published status

Frontend

Blog listing

Category filtering

Tag filtering

Search

Pagination

Blog detail

Related posts

Author section

Phase 10 — Careers

Careers page

Job listing

Job detail

Job categories

Location

Employment type

Experience

Skills

Application form

Job Application

Candidate name

Email

Phone

Resume upload

Cover letter

Portfolio URL

LinkedIn URL

Application status

Phase 11 — Contact

Contact Page

Contact form

Name

Email

Phone

Company

Service

Budget

Message

Backend

Contact model

REST API

Validation

Spam protection

Admin management

Email notification

Auto-response

Phase 12 — Django Models

Create models for:

SiteSettings

Service

Industry

Technology

Project

ProjectImage

CaseStudy

Testimonial

TeamMember

BlogPost

BlogCategory

BlogTag

Job

JobApplication

ContactInquiry

Phase 13 — REST API

Create APIs for:

/api/v1/services/

/api/v1/services/<slug>/

/api/v1/industries/

/api/v1/technologies/

/api/v1/projects/

/api/v1/projects/<slug>/

/api/v1/case-studies/

/api/v1/case-studies/<slug>/

/api/v1/testimonials/

/api/v1/team/

/api/v1/blog/

/api/v1/blog/<slug>/

/api/v1/careers/

/api/v1/careers/<slug>/

/api/v1/applications/

/api/v1/contact/

/api/v1/site-settings/

Phase 14 — Django Admin

Create a polished admin experience for:

Services

Industries

Technologies

Projects

Case Studies

Testimonials

Team

Blog

Careers

Applications

Contact inquiries

Site settings

Admin requirements:

Search

Filters

Sorting

Slug generation

Image previews

Publish status

Bulk actions

Timestamps

Phase 15 — SEO

Page titles

Meta descriptions

Open Graph metadata

Twitter/X metadata

Canonical URLs

Sitemap

Robots.txt

Structured data

Semantic HTML

Image alt text

SEO-friendly slugs

Phase 16 — Performance

Lazy load images

Optimize images

Code splitting

Lazy load routes

Minimize API requests

Add caching where appropriate

Compress assets

Lighthouse optimization

Target:

Performance 90+

Accessibility 90+

Best Practices 90+

SEO 90+

Phase 17 — Security

Environment variables

Secure secret key

Production DEBUG=False

CORS configuration

CSRF protection

Secure cookies

Input validation

File upload validation

Rate limiting

API permissions

SQL injection protection

XSS protection

Phase 18 — Responsive Design

Test:

Mobile 320px

Mobile 375px

Mobile 430px

Tablet 768px

Laptop 1024px

Desktop 1440px

Large desktop 1920px

Phase 19 — Testing

Backend

Model tests

Serializer tests

API tests

Authentication tests

Contact form tests

Job application tests

Frontend

Component tests

API tests

Form validation tests

Routing tests

Responsive tests

End-to-End

Homepage

Services

Portfolio

Blog

Contact form

Careers

Admin

Phase 20 — Pre-Deployment

Before deploying, verify the complete application locally.

Frontend

Run production build

Verify npm run build succeeds

Test production preview

Verify all React routes work

Verify API URL comes from environment variables

Verify no localhost API URLs remain

Verify no console errors

Verify all forms work

Verify mobile layout

Backend

Run python manage.py check

Run migrations

Run backend tests

Verify DEBUG=False production configuration

Verify allowed hosts

Verify CORS configuration

Verify static files

Verify media upload configuration

Verify Gunicorn starts correctly

Verify all API endpoints

Verify admin login

Verify email configuration

Verify environment variables

Database

Create production PostgreSQL database on Render

Configure production database environment variables

Run migrations against production database

Create production Django superuser

Verify database connection

Verify database backups/retention settings

Phase 21 — Vercel Deployment

The React frontend will be deployed to Vercel.

Vercel Setup

Create/import Git repository in Vercel

Select frontend project/root directory

Configure framework as Vite if not auto-detected

Configure build command

Configure output directory

Configure Node.js version if required

Add production environment variables

Frontend Environment

Configure:

VITE_API_URL=https://<render-backend-domain>

Replace local API URL with Render production API URL

Verify environment variables are available during build

Redeploy after environment variable changes

SPA Routing

Because React Router is used:

Configure Vercel SPA fallback/rewrite

Test direct navigation to nested routes

Test page refresh on nested routes

Verify 404 pages work correctly

Example routes to test:

/services/
/services/web-development/
/portfolio/
/portfolio/example-project/
/blog/
/blog/example-post/
/careers/

Vercel Domain

Connect production domain

Configure DNS

Verify HTTPS

Verify www/non-www redirect strategy

Verify canonical domain

Test production domain

Phase 22 — Render Deployment

The Django backend will be deployed to Render.

Render Web Service

Create Render Web Service

Connect Git repository

Select backend directory if using monorepo

Configure Python version

Configure build command

Configure Gunicorn start command

Configure environment variables

Configure health check endpoint

Verify service deployment

Recommended production start command:

gunicorn <django_project>.wsgi:application

Use the actual Django project module name.

Render PostgreSQL

Create Render PostgreSQL database

Connect database to Django service

Configure database environment variables

Run migrations

Verify database connectivity

Render Environment Variables

Configure production secrets such as:

DJANGO_SECRET_KEY=
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=
DATABASE_URL=
CORS_ALLOWED_ORIGINS=
CSRF_TRUSTED_ORIGINS=

EMAIL_HOST=
EMAIL_PORT=
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
DEFAULT_FROM_EMAIL=

Do not commit these values to Git.

Static Files

Configure Django static files

Run collectstatic

Verify static files in production

Verify Django Admin styling works

Media Files

Choose and configure a production-safe media storage strategy.

Do not rely on ephemeral local filesystem storage for permanent user uploads.

Configure production media storage

Verify project images

Verify blog images

Verify team images

Verify resume uploads

Verify uploaded files survive redeployment

Phase 23 — Vercel + Render Integration

Production architecture:

                    Users
                      │
                      ▼
              ┌───────────────┐
              │    Vercel     │
              │ React / Vite  │
              └───────┬───────┘
                      │
                      │ HTTPS REST API
                      ▼
              ┌───────────────┐
              │    Render     │
              │ Django + DRF  │
              │   Gunicorn    │
              └───────┬───────┘
                      │
                      ▼
              ┌───────────────┐
              │    Render     │
              │  PostgreSQL   │
              └───────────────┘

CORS

Add Vercel production URL to Django CORS allowlist

Add local development URL separately

Do not use CORS_ALLOW_ALL_ORIGINS=True in production

Example:

https://your-domain.com
https://www.your-domain.com
https://your-project.vercel.app

Only include domains that are actually required.

CSRF

Add production frontend/domain to CSRF_TRUSTED_ORIGINS

Use HTTPS production origins

Verify Django admin and all state-changing requests

Phase 24 — Production Verification

After both Vercel and Render deployments:

Frontend

Open production website

Verify homepage

Verify navigation

Verify every public route

Verify responsive layout

Verify animations

Verify images

Verify forms

Verify blog

Verify portfolio

Verify careers

Verify SEO metadata

Verify favicon

Verify sitemap

Verify robots.txt

Backend

Open production API

Verify API health endpoint

Verify services API

Verify portfolio API

Verify blog API

Verify careers API

Verify contact API

Verify Django Admin

Verify authentication where applicable

Integration

Submit contact form from production

Confirm inquiry reaches PostgreSQL

Confirm email notification works

Submit career application

Confirm resume upload works

Verify blog content from Django Admin appears on Vercel

Verify portfolio content from Django Admin appears on Vercel

Verify service content from Django Admin appears on Vercel

Phase 25 — Domain, DNS & HTTPS

Purchase/configure production domain

Connect domain to Vercel

Configure DNS records

Verify SSL certificate

Verify HTTPS

Configure canonical domain

Test HTTP → HTTPS redirect

Test www → canonical redirect

Test canonical → www if that is the chosen strategy

The frontend should be the public website domain.

The backend should use a separate API domain/subdomain if desired, for example:

https://www.example.com
https://api.example.com

Phase 26 — Monitoring & Maintenance

Configure Vercel deployment monitoring

Configure Render service monitoring

Configure backend logging

Configure error tracking if required

Monitor API response errors

Monitor database usage

Monitor deployment failures

Configure uptime monitoring

Configure database backups

Document rollback procedure

Phase 27 — Final Security Review

Before announcing the production website:

Confirm no secrets exist in Git history/current files

Confirm DEBUG=False

Confirm production CORS is restricted

Confirm CSRF trusted origins are correct

Confirm admin uses HTTPS

Confirm upload validation

Confirm API permissions

Confirm rate limiting/spam protection

Confirm secure cookies where applicable

Confirm dependency vulnerabilities are reviewed

Confirm sensitive error details are not exposed

Confirm database credentials are stored only in Render environment variables

Phase 28 — Final QA

No broken links

No console errors

No API errors

No missing images

All forms validated

Mobile navigation works

All animations work

Keyboard navigation works

Accessibility checked

SEO checked

Lighthouse checked

Production build tested

Vercel deployment tested

Render deployment tested

Production database tested

Contact submission tested

Career application tested

Admin tested

Definition of Done

The project is complete when:

React frontend is fully functional.

Django REST API is fully functional.

PostgreSQL stores all dynamic content.

Django Admin can manage all website content.

Contact and career forms work end-to-end.

Blog and portfolio are dynamic.

Website is fully responsive.

Website has production-ready SEO.

Website passes security and performance checks.

Frontend successfully deploys to Vercel.

Backend successfully deploys to Render.

Production PostgreSQL runs on Render.

Vercel communicates successfully with Render over HTTPS.

Production CORS and CSRF settings are correctly configured.

Media/uploads use production-safe storage.

Production environment variables are configured securely.

Domain and HTTPS are working.

Monitoring and rollback procedures are documented.