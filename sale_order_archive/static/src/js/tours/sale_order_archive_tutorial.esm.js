import {registry} from "@web/core/registry";
import {stepUtils} from "@web_tour/tour_service/tour_utils";

registry.category("web_tour.tours").add("sale_order_archive_tutorial", {
    url: "/odoo",

    steps: () => [
        stepUtils.showAppsMenuItem(),
        {
            content: "Open the Sales module to archive the quotation",
            trigger: ".o_app[data-menu-xmlid='sale.sale_menu_root']",
            run: "click",
        },
        {
            content: "Remove all filters",
            trigger: ".o_facet_remove",
            run: "click",
        },
        {
            content: "Choose the row with 'Quotation'",
            trigger: ".o_data_row:has(td:contains('Quotation')) input",
            run: "click",
        },
        {
            content: "Go to 'Action'",
            trigger: "div:nth-child(2) > .o-dropdown",
            run: "click",
        },
        {
            content: "Choose 'Cancel'",
            trigger: ".o-dropdown-item:contains('Cancel')",
            run: "click",
        },
        {
            content: "Confirm the cancellation",
            trigger: ".modal-footer .btn-primary",
            run: "click",
        },
        {
            content: "Wait for the row to appear as 'Cancelled'",
            trigger: ".o_technical_modal button[name='action_mass_cancel']",
        },
        {
            content: "Choose the row with 'Cancelled'",
            trigger: ".o_data_row:has(td:contains('Cancelled')) input",
            run: "click",
        },
        {
            content: "Go to 'Action",
            trigger: "div:nth-child(2) > .o-dropdown",
            run: "click",
        },
        {
            content: "Choose 'Archive'",
            trigger: ".o-dropdown-item:contains('Archive')",
            run: "click",
        },
        {
            content: "Confirm the archiving",
            trigger: ".modal-footer .btn-primary",
            run: "click",
        },
        {
            trigger: ".o_searchview_dropdown_toggler",
            run: "click",
        },
        {
            content: "Open the menu",
            trigger: ".o-dropdown-item:nth-child(9)",
            run: "click",
        },
        {
            trigger: ".o_list_renderer",
            run: "click",
        },
        {
            trigger: ".o_data_row:nth-child(1) input",
            run: "click",
        },
        {
            trigger: "div:nth-child(2) > .o-dropdown",
            run: "click",
        },
        {
            trigger: ".o-dropdown-item:nth-child(5)",
            run: "click",
        },
    ],
});
