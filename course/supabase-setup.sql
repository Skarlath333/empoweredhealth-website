-- Empowered Health: course sign-ups database (Supabase).
-- Run once in Supabase: SQL Editor > New query > paste this file > Run.
-- Visitors (the public "anon" key) can only ADD a sign-up. Only signed-in staff whose email is
-- in the staff table can READ sign-ups. Staff emails are added in the SQL editor, never in this repo.

create table if not exists public.course_signups (
  id bigint generated always as identity primary key,
  created_at timestamptz not null default now(),
  first_name text not null check (char_length(first_name) between 1 and 100),
  last_name  text not null check (char_length(last_name)  between 1 and 100),
  email      text not null check (char_length(email) between 3 and 254 and email like '%_@_%._%'),
  phone      text not null check (char_length(phone) between 7 and 40),
  role       text not null check (char_length(role) between 1 and 60),
  page       text check (page is null or char_length(page) <= 300)
);

create table if not exists public.staff (
  email text primary key
);

alter table public.course_signups enable row level security;
alter table public.staff enable row level security;

-- Anyone may add a sign-up (no reading, editing or deleting).
drop policy if exists "public can sign up" on public.course_signups;
create policy "public can sign up" on public.course_signups
  for insert to anon, authenticated
  with check (true);

-- Only staff can read sign-ups.
drop policy if exists "staff can read sign-ups" on public.course_signups;
create policy "staff can read sign-ups" on public.course_signups
  for select to authenticated
  using (exists (select 1 from public.staff s where lower(s.email) = lower(auth.jwt() ->> 'email')));

-- Staff can delete a sign-up (for example, when someone asks to be removed).
drop policy if exists "staff can delete sign-ups" on public.course_signups;
create policy "staff can delete sign-ups" on public.course_signups
  for delete to authenticated
  using (exists (select 1 from public.staff s where lower(s.email) = lower(auth.jwt() ->> 'email')));

-- Signed-in users can check whether they are staff; nobody can change the staff list from the website.
drop policy if exists "users see own staff row" on public.staff;
create policy "users see own staff row" on public.staff
  for select to authenticated
  using (lower(email) = lower(auth.jwt() ->> 'email'));

grant insert on public.course_signups to anon, authenticated;
grant select, delete on public.course_signups to authenticated;
grant select on public.staff to authenticated;
revoke select, update, delete on public.course_signups from anon;

-- After running the above, add yourself as staff (replace the email), then run just this line:
-- insert into public.staff (email) values ('you@example.com');
