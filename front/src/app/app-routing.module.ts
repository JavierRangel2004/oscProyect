import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './com/home/home.component';
import { NotFoundComponent } from './com/not-found/not-found.component';
import { OrganizationsComponent } from './com/organizations/organizations.component';
import { ProjectsComponent } from './com/projects/projects.component';
import { OrganizationDetailsComponent } from './com/organization-details/organization-details.component';
import { ProjectDetailsComponent } from './com/project-details/project-details.component';
import { SigninComponent } from './com/signin/signin.component';

const routes: Routes = [
  {path:'home', component: HomeComponent},
  {path:'organizations', component: OrganizationsComponent
  //   , children: [
  //   {path:':id', component: OrganizationDetailsComponent},
  // ]
  },
  // temporal:
  {path:'organizationsexample', component: OrganizationDetailsComponent},
  {path:'projects', component: ProjectsComponent
  //   , children: [
  //   {path:':id', component: ProjectDetailsComponent},
  // ]
  },
  // temporal:
  {path:'projectsexample', component: ProjectDetailsComponent},
  {path: 'signin', component:SigninComponent},
  {path: 'not-found', component:NotFoundComponent},
  {path: '', redirectTo: 'home', pathMatch: 'full'},
  {path: '**', redirectTo: 'not-found'}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
