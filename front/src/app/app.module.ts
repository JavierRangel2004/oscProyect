// src/app/app.module.ts
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './com/home/home.component';
import { NotFoundComponent } from './com/not-found/not-found.component';
import { NavbarComponent } from './com/navbar/navbar.component';
import { OrganizationsComponent } from './com/organizations/organizations.component';
import { ProjectsComponent } from './com/projects/projects.component';
import { OrganizationDetailsComponent } from './com/organization-details/organization-details.component';
import { ProjectDetailsComponent } from './com/project-details/project-details.component';
import { SigninComponent } from './com/signin/signin.component';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    NotFoundComponent,
    NavbarComponent,
    OrganizationsComponent,
    ProjectsComponent,
    OrganizationDetailsComponent,
    ProjectDetailsComponent,
    SigninComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
