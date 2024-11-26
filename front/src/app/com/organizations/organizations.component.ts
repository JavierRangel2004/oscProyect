// src/app/com/organizations/organizations.component.ts
import { Component, OnInit } from '@angular/core';
import { OrganizationService } from '../../services/organization.service';
import { Organization } from '../../models/organization';
import { environment } from '../../../environments/environment';

@Component({
  selector: 'app-organizations',
  templateUrl: './organizations.component.html',
  styleUrls: ['./organizations.component.css'],
})
export class OrganizationsComponent implements OnInit {
  organizations: Organization[] = [];

  constructor(private organizationService: OrganizationService) {}

// src/app/com/organizations/organizations.component.ts
ngOnInit(): void {
  this.organizationService.getOrganizations().subscribe(
    (data) => {
      this.organizations = data.sort((a, b) => a.name.localeCompare(b.name));
    },
    (error) => console.error('Error fetching organizations', error)
  );
}


  getLogoUrl(logoPath: string | null): string {
    if (logoPath) {
      return `${environment.mediaUrl}${logoPath}`;
    } else {
      return 'orgEX.jpg';
    }
  }
}
