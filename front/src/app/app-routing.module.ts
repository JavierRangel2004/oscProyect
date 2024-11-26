import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './com/home/home.component';
import { NotFoundComponent } from './com/not-found/not-found.component';
import { OrganizationsComponent } from './com/organizations/organizations.component';
import { ProjectsComponent } from './com/projects/projects.component';
import { OrganizationDetailsComponent } from './com/organization-details/organization-details.component';
import { ProjectDetailsComponent } from './com/project-details/project-details.component';
import { SigninComponent } from './com/signin/signin.component';

// src/app/app-routing.module.ts
const routes: Routes = [
  { path: 'home', component: HomeComponent },
  { path: 'organizations', component: OrganizationsComponent },
  { path: 'organizations/:id', component: OrganizationDetailsComponent },
  { path: 'projects', component: ProjectsComponent },
  { path: 'projects/:id', component: ProjectDetailsComponent },
  { path: 'login', component: SigninComponent },
  { path: 'not-found', component: NotFoundComponent },
  { path: '', redirectTo: 'home', pathMatch: 'full' },
  { path: '**', redirectTo: 'not-found' },
];


@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
